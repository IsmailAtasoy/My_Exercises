#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {

	int one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, dice;
	
	srand(time(NULL));

	for (int i = 0;i < 100;i++) {
		dice = 1 + rand() % 6;
		switch (dice) {

		case 1:
			one++;
			break;

		case 2:
			two++;
			break;

		case 3:
			three++;
			break;
				
		case 4:
			four++;
			break;

		case 5:
			five++;
			break;

		case 6:
			six++;
			break;

		default:
			break;
		}
	}
	printf("The possibilities of six faces dice: \n1: %d\n2: %d\n3: %d\n4: %d\n5: %d\n6: %d\n ", one, two, three, four, five, six);
}