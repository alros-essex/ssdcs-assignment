import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';


import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {MeasureComponent} from './measure/measure.component';
import {UsersComponent} from './users/users.component';
import {ExperimentsComponent} from './experiments/experiments.component';
import {LoginComponent} from './login/login.component';
import {FormsModule} from '@angular/forms';
import {DashboardComponent} from './dashboard/dashboard.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import { UserDetailComponent } from './user-detail/user-detail.component';
import { NewUserComponent } from './new-user/new-user.component';

@NgModule({
  declarations: [
    AppComponent,
    MeasureComponent,
    UsersComponent,
    ExperimentsComponent,
    LoginComponent,
    DashboardComponent,
    UserDetailComponent,
    NewUserComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatToolbarModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
