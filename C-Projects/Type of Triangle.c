#include <stdio.h>
int main(void) {
	int a, b, c, sum_all;
	printf("Please enter the angles of triangle!\n");

	scanf("%d\n%d\n%d", &a, &b, &c);

	sum_all = a + b + c;

	if (sum_all == 180) {
		{
			if (a == b && b == c) {
				printf("It is an equilateral triange.\n");
			}
			else if (a == b || a == c || b == c) {
				printf("It is an isosceles triangle.\n");
			}
			else if (a != b || a != c || b != c) {
				printf("It is a scalene triangle.\n");
			}
		}
	
	}
	else {
		printf("The triangle does not exist.\n");

	}
		return 0;
	}


















