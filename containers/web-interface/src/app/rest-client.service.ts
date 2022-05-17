import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {firstValueFrom, Observable, of} from 'rxjs';
import {logindetails} from './login/logindetails';
import {Experiments} from './experiments/experiments';
import {Measure} from './measure';
import {User} from './user';


@Injectable({
  providedIn: 'root'
})
export class RestClientService {

  private apiUrl = 'http://localhost:5000';
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    })
  };

  private bearerToken?: string;

// Make http class in the client

  constructor(private http: HttpClient) {
  }

  private set_bearer_token(): void {
    if (!!sessionStorage.getItem('token')) {
      this.bearerToken = sessionStorage.getItem('token');
    }
  }

  private make_headers(): HttpHeaders {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    });

    return headers.append('Authorization', `Bearer ${this.bearerToken}`);
  }

  // get login details and add an argument that takes in login details
  getlogin(details: logindetails): Observable<logindetails> {
    this.set_bearer_token();
    const url = `${this.apiUrl}/login`;
    this.logMessage(JSON.stringify(details));
    this.logMessage(url);
    // post the details to the server //tell python to interpret this as json
    return this.http.post<logindetails>(url, details, {headers: this.make_headers()});
  }

  getUsers(): Observable<User[]> {
    this.set_bearer_token();
    const url = `${this.apiUrl}/users/`;
    this.logMessage('Getting users from api');
    return this.http.get<User[]>(url, {headers: this.make_headers()});
  }

  // ngOnInit(): void {}
// get array of measures
  get_measures(): Observable<Measure[]> {
    this.set_bearer_token();
    const url = `${this.apiUrl}/measures/`;
    return this.http.get<Measure[]>(url, {headers: this.make_headers()});
  }

  get_measure_for_experiment(experimentId: string): Observable<Measure[]> {
    this.set_bearer_token();
    const url = `${this.apiUrl}/measures/${experimentId}`;

    this.logMessage(`Trying for ${url}`);
    return this.http.get<Measure[]>(url, {headers: this.make_headers()});
  }

  get_experiments(): Observable<Experiments[]> {
    this.set_bearer_token();
    const url = `${this.apiUrl}/experiments/`;
    return this.http.get<Experiments[]>(url, {headers: this.make_headers()});
  }

  save_experiment(name: string): void {
    this.set_bearer_token();
    const url = `${this.apiUrl}/experiments/`;
    const body = {name};

    this.logMessage(`POSTing to ${url} to save ${name}`);
    this.logMessage(JSON.stringify(body));

    this.http.post<any>(url, body, {headers: this.make_headers()})
      .subscribe(value => {
        this.logMessage(`response from experiment endpoint: ${value}`);
      });
  }

  putUser(userId: string, name: string, username: string, email: string): void {
    this.set_bearer_token();
    const url = `${this.apiUrl}/users/${userId}`;
    const payload = {name, username, email};
    this.logMessage('PUTting user');
    this.http.put<any>(url, payload, {headers: this.make_headers()})
      .subscribe(response => this.logMessage(`PUT user endpoint response: ${JSON.stringify(response)}`));
  }

  postUser(user: User): void {
    this.set_bearer_token();
    const url = `${this.apiUrl}/users/`;
    this.logMessage('POSTing user');
    this.http.post<any>(url, user, {headers: this.make_headers()})
      .subscribe(response => this.logMessage(`POST user endpoint response: ${JSON.stringify(response)}`));
  }

  private logMessage(message: string): void {
    console.log(`[RestClientService]: ${message}`);
  }
}
