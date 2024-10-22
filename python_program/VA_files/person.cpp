#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		int getDecades();
		int fib();
	private:
		int age;
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

int Person::getDecades(){
	return age/10;
	}

int Person::fib(){
	int a = 0;
	int b = 1;
	int c = 0;
	for (int i = 0; i < age; i++){
		c = a + b;
		a = b;
		b = c;
		}
	return c;
}

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	int Person_getDecades(Person* person) {return person->getDecades();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	int Person_fib(Person* person) {return person->fib();}
	}