package co.sr.algorithm;

import java.util.Scanner;

public class Lv4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int n = sc.nextInt();
		
		double tmp = 1.0;
		while (n-- > 0) {
			tmp *= x;
			System.out.println(n +"!");
		}
		System.out.println(tmp);
	}

}
