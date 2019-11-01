package co.sr.controller;

import java.io.IOException;
import java.util.HashMap;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.catalina.connector.Request;

import co.sr.command.Command;

@WebServlet("/MainController")
public class MainController extends HttpServlet {
	private static final long serialVersionUID = 1L;
	//HashMap 추가 
	private HashMap<String, Command> map = null;
	
    public MainController() {
        super();
    }

	public void init(ServletConfig config) throws ServletException {
		map = new HashMap<String, Command>();
		map.put("/index.do", new IndexCommand());
	}

	protected void service(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8"); 
		String uri = request.getRequestURI();
		String context = request.getContextPath();
		String path = uri.substring(context.length());
		
		Command comm = map.get(path);
		String page = comm.execute(request, response);
		
		if (page != null) {
			if(page.startsWith("redirect:")) {
				response.sendRedirect(page.substring(9));
			} else if(page.startsWith("ajax:")) {
				response.getWriter().append(page.substring(5));
			} else if(page.startsWith("script:")) {
				response.getWriter().append(page.substring(7));
			} else {
				RequestDispatcher dispatcher = request.getRequestDispatcher(page);
				dispatcher.forward(request, response);
			
			}
		}//	
	}
}
