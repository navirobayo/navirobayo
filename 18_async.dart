void main() async {
  DataService dataService = DataService();
  String data = await dataService.getData();
  print(data);
}

class DataService {
  Future _getDataFromCloud() async {
    // get data from cloud -> time
    await Future.delayed(Duration(seconds: 4));
    print("get data finished");
    return "fake data";
  }

  Future<String> _parsedDataFromCloud({required String dataFromCloud}) async {
    // parse data from cloud -> time
    await Future.delayed(Duration(seconds: 2));
    print("parse data finished");
    return "fake parsed";
  }

  Future<String> getData() async {
    final String dataFromCloud = await _getDataFromCloud();
    final String parsedData =
        await _parsedDataFromCloud(dataFromCloud: dataFromCloud);

    // alternative way syntax
    /* final String parsedData =
        await _getDataFromCloud().then((dataFromCloud) async {
      return await _parsedDataFromCloud(dataFromCloud: dataFromCloud);
    }); */

    return parsedData;
  }
}
