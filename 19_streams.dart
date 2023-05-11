import 'dart:async';

void main() {
  Stream numberStream = NumberGenerator().getStream.asBroadcastStream();
  // broadcast -> can handle multiple subscribers

  StreamSubscription sub1 = numberStream.listen(
    (event) {
      print(event);
    },
    onDone: () {
      // will be executed when the stream is finished
    },
    onError: (error) {
      // what should happen if an error occurs
    },
    cancelOnError: true,
  );
}

class NumberGenerator {
  int _counter = 0;
  StreamController<int> _controller = StreamController<int>();

  Stream<int> get getStream => _controller.stream;

  NumberGenerator() {
    final timer = Timer.periodic(Duration(seconds: 1), (timer) {
      _controller.sink.add(_counter);
      _counter++;
    });

    Future.delayed(Duration(seconds: 10), () => timer.cancel());
  }
}
