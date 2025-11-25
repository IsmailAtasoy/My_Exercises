#include <iostream>
#include <string>
using namespace std;

class CAMPINARIBANK {
public:
	string UserName;
	int AccountBalance = 0;
	int money;
	int currentbalance;
	int operation;
	
	CAMPINARIBANK() {
		cout << "--------------------\n";
		cout << "Enter your username :\n ";
		cout << "--------------------\n";
		getline(cin >> ws, UserName);
		cout << "--------------------\n";
		cout << "Welcome to CAMPINARIBANK " << UserName << " :)\n";
		while (operation != 3) {
			info();
		}

	}

	void info() {
		cout << "--------------------\n";
		cout << "Your account balance : " << AccountBalance << "\n";
		cout << "--------------------\n";
		cout << "Please select an operation :\n1-Deposit\n2-Withdraw\n3-Exit\n";
		cout << "--------------------\n";
		cin >> operation;
		switch (operation)
		{
		case 1:
			Deposit();
			break;
		case 2:
			Withdraw();
			break;
		default:
			break;
		}
	}	

	void Deposit() {
		cout << "--------------------\n";
		cout << "Write to money you want to deposite : \n";
		cin >> money;
		AccountBalance += money;
		cout << "--------------------\n";
	}

	void Withdraw() {
		cout << "--------------------\n";
		cout << "Write to money you want to withdraw : \n";
		cout << "--------------------\n";
		cin >> money;
		cout << "--------------------\n";
		currentbalance = AccountBalance;
		AccountBalance = currentbalance;
		AccountBalance -= money;
		if (AccountBalance < 0) {
			AccountBalance = currentbalance;
			while (money != 0) {
				cout << "--------------------\n";
				cout << "The proccess has been failed !!!\nPlease enter a valid money amount !!!\nTo cancel press 0\n";
				cout << "--------------------\n";
				Withdraw();
			}
		}
		cout << "--------------------\n";
	
	}

};

int main() {

	CAMPINARIBANK User1;
	CAMPINARIBANK User2;
}