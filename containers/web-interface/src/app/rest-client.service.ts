import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable, of, tap} from "rxjs";
import { Measure } from './measure';

@Injectable({
  providedIn: 'root'
})
export class RestClientService {

  private apiUrl = 'http://localhost:5000';
  private httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    })
  }
//Make http class in the client

  constructor(private http: HttpClient) {
  }

  ngOnInit(): void {
  }
//get array of measures
  getmeasures(): Observable<Measure[]> {
    const url = `${this.apiUrl}/measures`;
    return this.http.get<Measure[]>(url)
    
  }

}
