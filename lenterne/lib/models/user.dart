class User {
  String username;
  String refresh_token;
  String access_token;

  User(
      {required this.username,
      required this.refresh_token,
      required this.access_token});

  // conversion d'un User à un MAP

  Map<String, String> toMap() {
    return {
      "username": username,
      "refresh": refresh_token,
      "access_token": access_token
    };
  }
  // conversion d'un map ) un Iser

  static User fromMap(Map<String, dynamic> data) {
    return User(
        username: data["username"],
        refresh_token: data["refresh_token"],
        access_token: data["access_token"]);
  }
}
