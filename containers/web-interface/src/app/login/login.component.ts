import {Component, OnInit} from '@angular/core';
import {RestClientService} from '../rest-client.service';
import {logindetails} from './logindetails';
import {Input} from '@angular/core';
import {initializeApp} from 'firebase/app';
import {getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword} from 'firebase/auth';
import {FirebaseApp} from '@angular/fire/app';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
// create a variable
  login: logindetails = {username: 'phigg@home.cern', password: '123456'};

  bearerToken?: string;
  app?: FirebaseApp;
  auth?;

  firebaseConfig = {
    apiKey: 'AIzaSyDWxR3Y5dQj09Nr15VtC13VGnRWh9WgOV4',
    authDomain: 'coding-output.firebaseapp.com',
    databaseURL: 'https://coding-output-default-rtdb.firebaseio.com',
    projectId: 'coding-output',
    storageBucket: 'coding-output.appspot.com',
    messagingSenderId: '953911328931',
    appId: '1:953911328931:web:a4d2f0eb0bb35cdd1eff16',
    measurementId: 'G-T8DCDWNTQJ'
  };

  constructor(private rest: RestClientService) {
  } // linking rest client to login component
  // create a login function
  do_login(): void {
    this.app = initializeApp(this.firebaseConfig);
    this.auth = getAuth(this.app);

    signInWithEmailAndPassword(this.auth, this.login.username, this.login.password)
      .then(userCredential => {
        console.log('Logged in');
        userCredential.user.getIdToken()
          .then(token => {
            this.bearerToken = token;
            this.rest.set_bearer_token(token);
          });
      });
  }

  ngOnInit(): void {
  }

}


