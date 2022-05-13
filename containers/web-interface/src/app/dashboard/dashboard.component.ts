import {Component, OnInit} from '@angular/core';
import {AuthUtilsService} from '../auth-utils.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  loggedIn?: boolean;

  constructor(private authUtils: AuthUtilsService) {
  }

  ngOnInit(): void {
  }

  isUserLoggedIn(): boolean {
    return this.authUtils.isLoggedIn();
  }

  logUserOut(): void {
    this.authUtils.logout();
  }

}
