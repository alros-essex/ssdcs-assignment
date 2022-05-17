import {Component, OnInit} from '@angular/core';
import {User} from '../user';
import {UserUtilsService} from '../user-utils.service';
import {ActivatedRoute} from '@angular/router';
import {RestClientService} from '../rest-client.service';

@Component({
  selector: 'app-user-detail',
  templateUrl: './user-detail.component.html',
  styleUrls: ['./user-detail.component.css']
})
export class UserDetailComponent implements OnInit {

  user?: User;

  constructor(private userService: UserUtilsService,
              private rest: RestClientService,
              private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getUserDetails();
  }

  getUserDetails(): void {
    const userId = this.route.snapshot.paramMap.get('id');
    this.userService.getUsers()
      .subscribe(users => users.find(user => user.user_id === userId));
  }

  updateUser(): void {
    if (!this.user) {
      return;
    }

    this.rest.putUser(this.user.user_id,
      this.user.name,
      this.user.username,
      this.user.email);
  }
}
