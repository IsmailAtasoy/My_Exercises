#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int main(void) {

	int guess, number, range1, range2;

	srand(time(NULL));

	printf("Please enter your game range : x <= your guess <= y\n ");
	scanf_s("%d \n%d", &range1, &range2);

	number = range1 + rand() % (range2-range1+1);

	while (true) {
		
		printf("Make your guess !!!\nTo exit game enter -1 \n");
		scanf_s("%d",&guess);

		if (guess == -1) {
			printf("Game over\n");
			return 0;
		}

		if (number == guess) {
			printf("You won !!!\n");
			return 0;
		}
		else {
			printf("Your guess is incorrect !!! It was %d :(\n",number);
			number = range1 + rand() % (range2-range1+1);

		}


	}

	return 0;
}