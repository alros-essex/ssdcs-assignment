import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { TranslateModule } from '@ngx-translate/core';

import { CoreCommonModule } from '@core/common.module';

import { ContentHeaderModule } from 'app/layout/components/content-header/content-header.module';

import { ExperimentsComponent } from './experiments.component';
import { HomeComponent } from './home.component';

const routes = [
  {
    path: 'experiments',
    component: ExperimentsComponent,
    data: { animation: 'experiments' }
  },
  {
    path: 'home',
    component: HomeComponent,
    data: { animation: 'home' }
  }
];

@NgModule({
  declarations: [ExperimentsComponent, HomeComponent],
  imports: [RouterModule.forChild(routes), ContentHeaderModule, TranslateModule, CoreCommonModule],
  exports: [ExperimentsComponent, HomeComponent]
})
export class SampleModule {}
