import {Injectable} from '@angular/core';
import {RestClientService} from './rest-client.service';
import {User} from './user';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserUtilsService {

  // users?: User[];

  constructor(private rest: RestClientService) {
  }

  getUsers(): Observable<User[]> {
    // if (!this.users) {
    //   this.initUsers();
    //   return this.rest.getUsers();
    // } else {
    //   return of(this.users);
    // }
    return this.rest.getUsers();
  }

  // private initUsers(): void {
  //   this.rest.getUsers().subscribe(users => this.users = users);
  // }

  // getUserById(userId: string): User {
  //   this.logMessage(`Looking for user with ID ${userId}.`);
    // return !!this.users
    //   ? this.users.find(u => u.user_id === userId)
    //   : null;
  // }

  private logMessage(message: string): void {
    console.log(`[UserUtilsService]: ${message}`);
  }
}
