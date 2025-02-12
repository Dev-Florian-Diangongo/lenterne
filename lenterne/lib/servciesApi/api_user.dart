 import 'package:dio/dio.dart';

class ServiceApi {
  final _dio = Dio(
      BaseOptions(baseUrl: "", headers: {"Content-Type": "application/json"}));

  Future<Map<String, dynamic>> login(String username, String password) async {
    try {
      final response = await _dio.post("login_user/",
          data: {"username": username, "password": password});
          return response.data ;
    } catch (e) {
      return {};
    }
  }


  // logout user

}
