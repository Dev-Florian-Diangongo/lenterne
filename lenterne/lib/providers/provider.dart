import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:lenterne/models/user.dart';
import 'package:lenterne/servciesApi/api_user.dart';

class ProviderUser with ChangeNotifier {
  User? _user;
  final _storage = FlutterSecureStorage();
  User? get user => _user;

  Future<void> login(String username, String password) async {
    try {
      final apiservice = ServiceApi();
      final response = await apiservice.login(username, password);

      // enregistrement du token dans secure
      final refresh_token = response['refresh'];
      final access_token = response["access"];

      _user = User(
          username: username,
          refresh_token: refresh_token,
          access_token: access_token);
      await _storage.write(key: 'access_token', value: access_token);
      await _storage.write(key: 'refresh_token', value: refresh_token);
      notifyListeners();
    } catch (e) {
      return null;
    }
  }

  Future<void> logout() async {
    await _storage.delete(key: "access_token");
    await _storage.delete(key: "refresh_token");
    _user = null;
    notifyListeners();
  }

  Future<void> checkStatusUser() async {
    final access_token = await _storage.read(key: 'access_token');
    final refresh_token = await _storage.read(key: 'refresh_token');
    if (access_token != null && refresh_token != null) {
      _user = User(
          username: "",
          refresh_token: refresh_token,
          access_token: access_token);
      notifyListeners();
    }
  }
}
