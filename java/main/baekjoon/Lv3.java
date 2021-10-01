package main.baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Lv3 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		/* 입출력용 1~4번 스캐너, 5~11번 버퍼사용 */
		Scanner sc = new Scanner(System.in);
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		
		// 1. https://www.acmicpc.net/problem/2739
		int nn = sc.nextInt();
		for (int mm = 1; mm < 10; mm++) {
			System.out.println(nn + " * " + mm + " = " + nn*mm);
		}
		
		
		// 2. https://www.acmicpc.net/problem/10950
		int set = sc.nextInt();
		
		for(int i = 0; i<set; i++ ) {
			int aa = sc.nextInt();
			int bb = sc.nextInt();
			
			System.out.println(aa+bb);
		}
		
		
		// 3. https://www.acmicpc.net/problem/8393
		int number = sc.nextInt();
		int sum = 0;
		
		for (int i=1; i<=number; i++) {
			sum += i;
		}
		System.out.println(sum);
		
		
		// 4. https://www.acmicpc.net/problem/15552
		int testCase = Integer.parseInt(br.readLine());
		
		for(int i=0; i<testCase; i++) {
			
			String s = br.readLine();
			StringTokenizer st = new StringTokenizer(s);
			
			int first = Integer.parseInt(st.nextToken());
			int second = Integer.parseInt(st.nextToken());
			
			bw.write(first+second + "\n");
		}
		bw.flush();
		
		
		// 5. https://www.acmicpc.net/problem/2741		
		int line = Integer.parseInt(br.readLine());
		
		for(int i=1; i<=line; i++) {
			bw.write(i+"\n");
			bw.flush();
		}
		
		
		// 6. https://www.acmicpc.net/problem/2742
		int text = Integer.parseInt(br.readLine());
		
		for(int i=0; text>i; text--) {
			bw.write(text+"\n");
			bw.flush();
		}
		
		
		// 7. https://www.acmicpc.net/problem/11021
		int sets = Integer.parseInt(br.readLine());
		
		for(int i=1; i<=sets; i++) {
			String str = br.readLine();
			StringTokenizer st = new StringTokenizer(str);
			
			int first = Integer.parseInt(st.nextToken());
			int second = Integer.parseInt(st.nextToken());
			
			bw.write("Case #" + i + ": " + (first+second) + "\n");
			bw.flush();
		}
		
		//8. https://www.acmicpc.net/problem/11022
		int setLine = Integer.parseInt(br.readLine());
		
		for(int i=1; i<=setLine; i++) {
			String str = br.readLine();
			StringTokenizer st = new StringTokenizer(str);
			
			int first = Integer.parseInt(st.nextToken());
			int second = Integer.parseInt(st.nextToken());
			
			bw.write("Case #" + i + ": " + first + " + " + second + " = " + (first+second) + "\n");
			bw.flush();
		}
		
		// 9. https://www.acmicpc.net/problem/2438
		int star = Integer.parseInt(br.readLine());
		
		for(int i=1; i<=star; i++) {
			for(int m=1; m<=i; m++) {
				bw.write("*");
				bw.flush();
			}
			bw.write("\n");
		}
		
		
		//10. https://www.acmicpc.net/problem/2439
		int route = Integer.parseInt(br.readLine());
		int stars = route;
		for(int i=1; i<=route; i++) {
			for(int m=1; m<=route; m++) {
				
				if (m <stars) {
					bw.write(" ");
				} else {
					bw.write("*");
				}
				bw.flush();
			}
			stars-=1;
			bw.write("\n");
		}
		
		// 11. https://www.acmicpc.net/problem/10871
		// 첫째줄 숫자 두개
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str);
		
		int n = Integer.parseInt(st.nextToken()); // 수열의 숫자개수
		int x = Integer.parseInt(st.nextToken()); // 출력 기준값; x보다 작은 숫자만 출력가능
		
		// 두번째줄 수열; 배열에 담아서 사용
		String arrLine = br.readLine(); // 수열 스트링으로 받음
		String[] arr = arrLine.split(" "); // 배열에 숫자 잘라서 넣음
		
		// 각 배열값이 기준값x보다 작으면 출력
		for(int i=0; i<arr.length; i++) {
			int score = Integer.parseInt(arr[i]); //배열값 숫자로 형변환
			if(score < x ) {
				bw.write(score + " ");
			} 
			bw.flush();
		}
	}
}
