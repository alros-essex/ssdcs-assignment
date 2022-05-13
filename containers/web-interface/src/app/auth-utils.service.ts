import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthUtilsService implements CanActivate {

  constructor(private router: Router) {
  }

  // tslint:disable-next-line:typedef
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    const token = sessionStorage.getItem('token');
    console.log(`Auth token in session storage: ${token}`);
    if (token) {
      // assume that user is logged in if token is not null
      console.log('Token present, user is logged in');
      return true;
    }

    console.log('Token not present, redirecting to login page');
    this.router.navigate(['/login']);
    return false;
  }

  logout(): void {
    sessionStorage.removeItem('token');
    this.router.navigate(['/login']);
  }

  isLoggedIn(): boolean {
    return !!sessionStorage.getItem('token');
  }
}
