import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MeasureComponent} from './measure/measure.component';

const routes: Routes = [
  {
    path: 'measures/:id',
    component: MeasureComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
