void main() {
  List<dynamic> exampleList = [1, 2, 3, 4];
  print(exampleList);

  print(exampleList[1]);

  print(exampleList.length);
  exampleList.add("value");
  print(exampleList);

  Map<String, dynamic> exampleMap = {
    "key1": 3,
    "key2": "fatty",
    "key3": "freedom"
  };

  print(exampleMap);
  print(exampleMap["key2"]);
  print(exampleMap.keys);
}
