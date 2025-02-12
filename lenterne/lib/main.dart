import 'package:flutter/material.dart';
import 'package:lenterne/esaie.dart';
import 'package:lenterne/pages/login.dart';
import 'package:lenterne/providers/provider.dart';
import 'package:provider/provider.dart';

void main() {
  loginEssaie("messie", "123456");
  // runApp(ChangeNotifierProvider(
  //   create: (context) => ProviderUser(),
  //   child: const MyApp(),
  // ));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Consumer<ProviderUser>(
        builder: (context, authProvider, child) {
          return authProvider.user == null ? LoginPage() : HomePage();
        },
      ),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text("Home page"),
    );
  }
}
