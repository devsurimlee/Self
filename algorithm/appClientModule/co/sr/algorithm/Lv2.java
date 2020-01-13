package co.sr.algorithm;

import java.util.Scanner;

public class Lv2 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
	
		/* 1330 : 두 수 비교하기 */
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		if (a > b)
			System.out.println(">");
		
		else if (a < b)
			System.out.println("<");
		
		else if (a == b) 
			System.out.println("==");
		
		
		/* 9498 : 시험 성적 */
		int score = sc.nextInt();
		if (100 >= score && score >= 90)
			System.out.println("A");
		
		else if(100 >= score && score >= 80)
			System.out.println("B");
		
		else if(100 >= score && score >= 70)
			System.out.println("C");
		
		else if(100 >= score && score >= 60)
			System.out.println("D");
		
		else if (59 >= score)
			System.out.println("F");
		
		
		/* 2753 : 윤년 */
		int year = sc.nextInt();
		
		if( year % 4 == 0 && 
				(year % 100 != 0 || year % 400 == 0) ) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
		
		/* 2884: 알람 시계 */
		int h = sc.nextInt();
		int m = sc.nextInt();
		
		if (m >= 45) {
			m -= 45;
			
		} else {
			
			if (h == 0 ) {
				h = h + 24 -1;
				m = m + 60 - 45;
			} else {
				h -= 1; 
				m = m + 60 - 45;
			}
		}
		
		System.out.println(h +" "+ m);
		
		/* 10817 : 세 수 */
		
		
		
	}
}

