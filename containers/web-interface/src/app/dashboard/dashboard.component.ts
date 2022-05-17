import {Component, OnInit} from '@angular/core';
import {AuthUtilsService} from '../auth-utils.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

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

  getUserName(): string {
    return this.authUtils.getLoggedInUserDetails()?.username;
  }

  isUserAdmin(): boolean {
    return this.authUtils.isLoggedInUserAdmin();
  }

  private logMessage(message: string): void {
    console.log(`[DashboardComponent]: ${message}`);
  }

}
