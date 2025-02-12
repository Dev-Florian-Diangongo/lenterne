import 'package:flutter/material.dart';
import 'package:lenterne/providers/provider.dart';
import 'package:provider/provider.dart';

class LoginPage extends StatelessWidget {
  final _controllerUsername = TextEditingController();
  final _controllerPassword = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: TextFormField(
              controller: _controllerUsername,
              decoration: InputDecoration(
                hintText: "username",
                suffixIcon: Icon(Icons.person),
                border: OutlineInputBorder(),
              ),
            ),
          ),
          SizedBox(
            height: 12,
          ),
          Padding(
            padding: const EdgeInsets.all(12),
            child: TextFormField(
              controller: _controllerPassword,
              decoration: InputDecoration(
                hintText: "username",
                suffixIcon: Icon(Icons.person),
                border: OutlineInputBorder(),
              ),
            ),
          ),
          ElevatedButton(
              onPressed: () {
                final username = _controllerUsername.text;
                final password = _controllerPassword.text;
                Provider.of<ProviderUser>(context, listen: false)
                    .login(username, password);
              },
              child: Text("se connecter"))
        ],
      ),
    );
  }
}
