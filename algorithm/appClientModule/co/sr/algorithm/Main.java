package co.sr.algorithm;

import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int first = sc.nextInt();
		int second = sc.nextInt();
		int third = sc.nextInt();
		
		// 세 수 평균값; 평균값과 비교하여 큰/작 비교함
		float average = (first+second+third) / 3;
		
		// 큰 ? ?
		if (first >= average) {
			// 큰 큰 ?
			if (second >= average) {
				// 큰 큰 큰 ==> 평 평 평
				if (third >= average) {
					System.out.println(third);
				// 큰 큰 작; 첫번째 두번째 비교
				} else if (first > second) {
					System.out.println(second);
				} else 
					System.out.println(first);
			// 큰 작 큰; 첫번째 세번째 비교	
			} else if (third >= average) {
				if (first > third) {
					System.out.println(third);
				} else 
					System.out.println(first);
			} else 
				System.out.println(third);
		// 작 큰 ?
		} else if (first < average && second >= average) {
			// 작 큰 큰; 두번째 세번째 비교
			if (third >= average) {
				if (second > third) {
					System.out.println(third);
				} else
					System.out.println(second);
			// 작 큰 작; 첫번째 세번째 비교
			} else 
				if (first > third) {
					System.out.println(first);
				} else 
					System.out.println(third);
		// 작 작 큰 ; 첫번째 두번째 비교
		} else {
			if (first > second) {
				System.out.println(first);
			} else
				System.out.println(second);
		}
	}
}
