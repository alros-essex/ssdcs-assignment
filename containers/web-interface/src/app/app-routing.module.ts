import {NgModule} from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import {MeasureComponent} from './measure/measure.component';
import {ExperimentsComponent} from './experiments/experiments.component';
import {LoginComponent} from './login/login.component';
import {AuthUtilsService} from "./auth-utils.service";

const routes: Routes = [
  {
    path: 'measures/:id',
    component: MeasureComponent,
    canActivate: [AuthUtilsService]
  },
  {
    path: 'experiments',
    component: ExperimentsComponent,
    canActivate: [AuthUtilsService]
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: '', redirectTo: '/login', pathMatch: 'full'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
