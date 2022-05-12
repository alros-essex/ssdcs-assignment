import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import { logindetails } from './login/logindetails';
import { Experiments } from './experiments/experiments';
import { Measure } from './measure';


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

  set_bearer_token(token: string): void {
    this.bearerToken = token;
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
    const url = `${this.apiUrl}/login`;
    console.log(details);
    console.log(url);
    // post the details to the server //tell python to interpret this as json
    return this.http.post<logindetails>(url, details, this.httpOptions);
  }

  // ngOnInit(): void {}
// get array of measures
  get_measures(): Observable<Measure[]> {
    const url = `${this.apiUrl}/measures/`;
    return this.http.get<Measure[]>(url, {headers: this.make_headers()});
  }

  get_measure_for_experiment(experimentId: string): Observable<Measure[]> {
    const url = `${this.apiUrl}/measures/${experimentId}`;

    console.log(`Trying for ${url}`);
    return this.http.get<Measure[]>(url, {headers: this.make_headers()});
  }

  get_experiments(): Observable<Experiments[]> {
    const url = `${this.apiUrl}/experiments/`;
    return this.http.get<Experiments[]>(url, {headers: this.make_headers()});
  }

  save_experiment(name: string): void {
    const url = `${this.apiUrl}/experiments/`;
    const body = {name};

    console.log(`POSTing to ${url} to save ${name}`);
    console.log(body);

    this.http.post<any>(url, body, {headers: this.make_headers()})
      .subscribe(value => {
        console.log(value);
      });
      // .pipe(response => {
      //   console.log(response);
      //   return response;
      // });
  }
}
