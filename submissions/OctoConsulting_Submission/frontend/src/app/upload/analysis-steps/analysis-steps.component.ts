import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { APIService } from 'src/app/services/api.service';

@Component({
  selector: 'app-analysis-steps',
  templateUrl: './analysis-steps.component.html',
  styleUrls: ['./analysis-steps.component.scss']
})
export class AnalysisStepsComponent implements OnInit {
  public step = 0;
  public result = null;
  @Output() done = new EventEmitter();
  @Input() resId = '';
  constructor(private apiService: APIService) { }

  ngOnInit() {
    const interval = setInterval( () => {
      this.step += 1;
      if (this.step >= 6 && this.result) {
        clearInterval(interval);
      }
    }, 5000);

    const APIPollInterval = setInterval( () => {
      if (this.result) {
        clearInterval(APIPollInterval);
      } else {
        this.pollForResults();
      }
    }, 10000);

    const checkForResult = setInterval( () => {
      if (this.step >= 6 && this.result) {
        this.done.emit(this.result);
        clearInterval(checkForResult);
      }
    }, 1000);
  }

  public pollForResults() {
    this.apiService.pollResults(this.resId)
      .subscribe(
        response => {
          if (response.Item) {
            this.result = response.Item;
          }
        },
        error => console.log(error)
      );
  }
}
