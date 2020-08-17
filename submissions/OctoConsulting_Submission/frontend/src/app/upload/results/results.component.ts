import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { APIService } from 'src/app/services/api.service';
import {PdfViewerComponent} from 'ng2-pdf-viewer';
import { ChartType, ChartPoint } from 'chart.js';




@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.scss']
})
export class ResultsComponent implements OnInit {
  @Input() file = null;
  @Input() result = null;
  public pdfSrc = null;
 
  constructor(private apiService: APIService) { }

  data = [] //[
  //   {
  //     clause: "EULA, pronounced YOOLA",
  //     score: 0.8
  //   },
  //   {
  //     clause: "YOOLA, pronounced EULA",
  //     score: 0.3
  //   }
  // ]

  @ViewChild(PdfViewerComponent) private pdfViewer: PdfViewerComponent;
  

  search(stringToSearch: string) {
    console.log(0);
    
    // [...document.getElementsByClassName('highlight')].forEach(e=>e.classList.remove('highlight'))

    this.pdfViewer.pdfFindController.executeCommand('find', {
      caseSensitive: false, findPrevious: undefined, highlightAll: true, phraseSearch: true, query: stringToSearch
    });
    
    setTimeout(()=>{
      document.getElementsByClassName('highlight middle selected')[0].scrollIntoView({behavior:"smooth"})
    }, 1000)
  }

  ngOnInit() {
    this.apiService.getJSON().subscribe(res => {
        console.log("======================")
        this.data = res as [{clause: string, score: number}]
    })
  
    this.onFileSelected();
    // this.apiService.pollResults('RGlya19EaWdnbGVyX1Jlc3VtZQ==').subscribe(
    //   response => {
    //     if (response.Item) {
    //       this.result = response.Item;
    //             }
    //   }
    // );

  }

  public chartClicked({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public chartHovered({ event, active }: { event: MouseEvent, active: {}[] }): void {
    console.log(event, active);
  }

  public onFileSelected() {
    if (this.file) {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.pdfSrc = e.target.result;
      };
      reader.readAsArrayBuffer(this.file);
    }
  }


  public nlpCompare(input): boolean {
    return +input > 4;
  }

  // public getGrade(grade: string) {
  //   const intGrade = Number(grade);
  //   let retVal = 'N/A';
  //   if (intGrade < 0.65) {
  //     retVal = 'F';
  //   } else if (intGrade >= 0.60 && intGrade < 0.70) {
  //     retVal = 'D';
  //   } else if (intGrade >= 0.70 && intGrade < 0.80) {
  //     retVal = 'C';
  //   } else if (intGrade >= 0.80 && intGrade < 0.90) {
  //     retVal = 'B';
  //   } else if (intGrade >= 0.90) {
  //     retVal = 'A';
  //   }
  //   return retVal;
  // }
}
