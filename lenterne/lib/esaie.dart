import 'package:dio/dio.dart';

Future<void> loginEssaie(String username, String password) async {
  final _dio = Dio(BaseOptions(
      baseUrl: "http://127.0.0.1:8000/",
      headers: {"Content-Type": "application/json"}));
  final response = await _dio.post("user/login_user/",
      data: {"username": username, "password": password});
  if (response.statusCode == 200) {
    print(response.data["access"]);
    print(response.data["refresg"]);
    print(response.data["detail"]);
  }
}
