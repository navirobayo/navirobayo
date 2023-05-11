void main() {
  Student estudiante1 = Student();
  estudiante1.setSemester = 2;
  estudiante1.setAge = 2;
  estudiante1.setSemester = 2;
  Person persona1 = Person();
  persona1.setName = "Natalia";
  persona1.setAge = 3;

  estudiante1.run();
  estudiante1.jump();
  estudiante1.party();

  persona1.run();
}

mixin Learner {
  void study() {
    print("study");
  }
}

mixin Jumper {
  void jump() {
    print("I can jump!");
  }
}

class Person {
  late String _name;
  late int _age;

  String get getName => this._name;
  int get getAge => this._age;

  set setName(String name) {
    this._name = name;
  }

  set setAge(int age) {
    this._age = age;
  }

  void run() {
    print("$_name runs!");
  }
}

class Student extends Person with Learner, Jumper {
  late int _semester;

  int get getSemester => this._semester;

  set setSemester(int semester) {
    this._semester = semester;
  }

  void party() {
    print("$_name is on a party!");
  }
}
