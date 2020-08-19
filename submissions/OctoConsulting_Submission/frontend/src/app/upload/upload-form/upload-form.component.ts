import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { environment } from '../../../environments/environment';
import { EncryptionService } from 'src/app/services/end-dec.service';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-upload-form',
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.scss']
})
export class UploadFormComponent implements OnInit {
  private postUrl = environment.POST_URL;
  private testUrl = 'http://localhost:5000';
  @Output() resId = new EventEmitter();
  @Output() step = new EventEmitter();

  constructor(private encryptionService: EncryptionService, private http: HttpClient) { }

  ngOnInit() {
  }


  public uploadNotification(event: any): void {
    this.step.emit(event.file);

    // this.http.post(environment.POST_URL, event.file).subscribe()
  }

  // public getUrl(name): string {
  //   const encrypted = btoa(name.split('.')[0]);
  //   this.resId.emit(encrypted);
  //   // return this.testUrl + `/${encrypted}.pdf`;
  //   return this.postUrl + `/${encrypted}.pdf`; 
  // }
  public getUrl(name): string { return this.postUrl + "/upload"; }
}
