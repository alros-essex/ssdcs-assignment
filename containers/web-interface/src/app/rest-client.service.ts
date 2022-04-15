import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable, of} from "rxjs";
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
  }
//Make http class in the client

  constructor(private http: HttpClient) {
  }

  //get login details and add an argument that takes in login details
  getlogin(details: logindetails): Observable<logindetails> {
    const url = `${this.apiUrl}/login`;
    console.log(details)
    console.log(url)
    return this.http.post<logindetails>(url, details, this.httpOptions) //post the details to the server //tell python to interpret this as json 
    }

  ngOnInit(): void {
  }
//get array of measures
  getmeasures(): Observable<Measure[]> {
    const url = `${this.apiUrl}/measures`;
    return this.http.get<Measure[]>(url)
    
  }

  getexperiments(): Observable<Experiments[]> {
    const url = `${this.apiUrl}/experiments`;
    return this.http.get<Experiments[]>(url)
    
  }
}
