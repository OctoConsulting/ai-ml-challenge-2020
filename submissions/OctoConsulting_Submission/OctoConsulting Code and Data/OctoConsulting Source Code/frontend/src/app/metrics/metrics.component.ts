import { Component, OnInit, ViewChild} from '@angular/core';
import { APIService } from 'src/app/services/api.service';
import { MatSort, MatTableDataSource, MatPaginator } from '@angular/material';



@Component({
  selector: 'app-metrics',
  templateUrl: './metrics.component.html',
  styleUrls: ['./metrics.component.scss']
})
export class MetricsComponent implements OnInit {

  public result = null;
  public logistic = [];
  public arrBar = [];
  public arrPie = [];
  public simrank = [];
  public resname = [];
  public skills = [];
  public pieGood = [];
  public pieBad = [];
  public headElements = ['Id', 'logistic', 'skill', 'nlp', 'govcon', 'certs'];
  dataSource = null;




 
  constructor(private apiService: APIService) { }

  @ViewChild(MatSort) sort: MatSort;
  ngOnInit() {
    // this.apiService.pollResults('all').subscribe(
    //      response => {
    //        if (response.Items) {
    //          this.result = response.Items;
    //          this.dataSource = new MatTableDataSource(this.result);
    //          this.dataSource.sort = this.sort;
    //          this.result.forEach(res => {
    //             this.logistic.push(res.logistic.S * 100);
    //             if (res.logistic.S < 0.70) {
    //               this.pieBad.push(res.logistic.S * 100);
    //             } else {
    //               this.pieGood.push(res.logistic.S * 100);
    //             }
    //             this.resname.push(atob(res.uuid.S));
    //             this.skills.push(res.skill_metrics.S);
    //          });

            
    //        }
    //      }
    //    );
  }

  convertString(name: string): string {
    return atob(name);
  }

  private customBarColor(array: any) {
    array.forEach( element => this.arrBar.push('#e07b00'));
  }
}
