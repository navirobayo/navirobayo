void main() {
  List<int> listOne = [1, 5, 8, 3, 7, 4, 4, 6, 7, 9, 0, 6, 5, 3, 2, 1];
  List<int> listTwo = [];

  for (int i = 0; i < listOne.length; i++) {
    if (listOne[i] == 4) {
      listTwo.add(listOne[i]);
    }
    print("List element: ${listOne[i]}");
  }
  print("Second list: $listTwo");
}
