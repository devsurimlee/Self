package main.leetCode.easy;

public class E0605CanPlaceFlowers {

    public static boolean canPlaceFlowers(int[] flowerbed, int n) {

        int sum = 0;

        // 꽃을 하나도 안심으므로 항상 true;
        if (n == 0) {
            return true;
        }

        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0) {
                // 제일 양쪽의 경우 왼쪽 오른쪽을 체크 안해도 되므로 or로 처리
                if ((i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                    sum++;
                    i++;
                }
            }
        }

        return sum >= n;
    }

    public static void main(String[] args) {

        int[] flowerbed = {1,0,0,0,1};
        int n = 1;

        System.out.println(canPlaceFlowers(flowerbed, n));

    }
}
