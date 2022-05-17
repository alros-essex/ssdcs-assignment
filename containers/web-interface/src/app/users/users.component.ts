import {Component, OnInit} from '@angular/core';
import {RestClientService} from '../rest-client.service';
import {User} from '../user';
import {AuthUtilsService} from '../auth-utils.service';
import {UserUtilsService} from '../user-utils.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {

  users?: User[];

  constructor(private rest: RestClientService, private userService: UserUtilsService) {
  }

  getUserById(userId: string): User {
    return this.users?.find(u => u.user_id === userId);
  }

  ngOnInit(): void {
    this.userService.getUsers()
      .subscribe(users => {
        this.logMessage(`Comprehensive list of all the users: ${JSON.stringify(users)}`);
        this.users = users;
      });
  }

  private logMessage(message: string): void {
    console.log(`[UsersComponent]: ${message}`);
  }
}



