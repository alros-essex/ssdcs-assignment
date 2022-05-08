import {Component, OnInit} from '@angular/core';
import {RestClientService} from '../rest-client.service';
import {Measure} from '../measure';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-measure',
  templateUrl: './measure.component.html',
  styleUrls: ['./measure.component.css']
})
export class MeasureComponent implements OnInit {

  measures: Measure[] = [];

  constructor(private rest: RestClientService,
              private route: ActivatedRoute
  ) {
  }

  // declaring a variable and get the rest service to assign measures to the variable
  // subscribe to show an error
  get_measure_for_experiment(): void {
    const experimentId = this.route.snapshot.paramMap.get('id');
    console.log(`Getting measures for experiment ${experimentId}`);
    this.rest.get_measure_for_experiment(experimentId)
      .subscribe(m => this.measures = m);
  }

  ngOnInit(): void {
    this.get_measure_for_experiment();
  }

}
