import {Component, OnInit} from '@angular/core';
import {RestClientService} from '../rest-client.service';
import {logindetails} from './logindetails';
import {initializeApp} from 'firebase/app';
import {getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword} from 'firebase/auth';
import {FirebaseApp} from '@angular/fire/app';
import {Router} from '@angular/router';
import {AuthUtilsService} from '../auth-utils.service';
import {User} from '../user';
import {Observer} from 'rxjs';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
// create a variable
  login: logindetails = {username: 'aalcorn@home.cern', password: '123456'};

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

  constructor(private rest: RestClientService,
              private authService: AuthUtilsService,
              private router: Router) {
  } // linking rest client to login component
  // create a login function
  do_login(): void {
    this.app = initializeApp(this.firebaseConfig);
    this.auth = getAuth(this.app);

    signInWithEmailAndPassword(this.auth, this.login.username, this.login.password)
      .then(userCredential => {
        this.logMessage(`Logged in. Credentials: ${JSON.stringify(userCredential)}`);

        userCredential.user.getIdToken()
          .then(token => {
            this.bearerToken = token;
            sessionStorage.setItem('token', token);
            this.setUserObjectAndNavigateToExperimentsPage(userCredential.user.email);
          });

      });
  }

  ngOnInit(): void {
  }

  private setUserObjectAndNavigateToExperimentsPage(email: string): void {
    const userObserver: Observer<User[]> = {
      next: users => {
        this.logMessage(`received users from API: ${JSON.stringify(users)}`);
        const filteredUser = this.filterByEmail(users, email);
        this.logMessage(`Filtered user by email: ${JSON.stringify(filteredUser)}`);
        if (!!filteredUser) {
          this.logMessage('User is present, logging in.');
          this.authService.setLoggedInUserDetails(filteredUser.email, filteredUser.role);
          this.router.navigate(['/experiments']);
        } else {
          this.logMessage('Error filtering user by email. Not logging in.');
        }
      },
      error: err => {
        this.logMessage(`Error calling users API (${JSON.stringify(err)}). Logging user in as scientist`);
        this.authService.setLoggedInUserDetails(
          email,
          'SCIENTIST'
        );
        this.router.navigate(['/experiments']);
      },
      complete: () => this.logMessage('Users API called')
    };

    this.rest.getUsers()
      .subscribe(userObserver);
  }

  private filterByEmail(users: User[], email: string): User {
    return users.find(u => u.email === email);
  }

  private logMessage(message: string): void {
    console.log(`[LoginComponent]: ${message}`);
  }

}


