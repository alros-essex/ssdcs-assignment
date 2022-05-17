import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import {RestClientService} from './rest-client.service';
import {LoggedInUserDetails} from './login/logged-in-user-details';

@Injectable({
  providedIn: 'root'
})
export class AuthUtilsService implements CanActivate {

  constructor(private router: Router, private rest: RestClientService) {
  }

  // tslint:disable-next-line:typedef
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    const token = sessionStorage.getItem('token');
    this.logMessage(`Auth token in session storage: ${token}`);
    if (token) {
      // assume that user is logged in if token is not null
      this.logMessage('Token present, user is logged in');
      return true;
    }

    this.logMessage('Token not present, redirecting to login page');
    this.router.navigate(['/login']);
    return false;
  }

  logout(): void {
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('loggedInUser');
    this.router.navigate(['/login']);
  }

  isLoggedIn(): boolean {
    return !!sessionStorage.getItem('token');
  }

  setLoggedInUserDetails(email: string, type: string): void {
    const userDetails: LoggedInUserDetails = {username: email, type};
    if (!!email && !!type) {
      sessionStorage.setItem('loggedInUser', JSON.stringify(userDetails));
    }
  }

  getLoggedInUserDetails(): LoggedInUserDetails {
    const userDetails = sessionStorage.getItem('loggedInUser');
    this.logMessage(`logged in user details: ${userDetails}`);
    return !!userDetails
      ? JSON.parse(userDetails) as LoggedInUserDetails
      : null;
  }

  isLoggedInUserScientist(): boolean {
    return this.isLoggedIn() && this.getLoggedInUserDetails()?.type === 'SCIENTIST';
  }

  isLoggedInUserAdmin(): boolean {
    return this.isLoggedIn() && this.getLoggedInUserDetails()?.type === 'ADMIN';
  }

  private logMessage(message: string): void {
    console.log(`[AuthUtilsService]: ${message}`);
  }
}
