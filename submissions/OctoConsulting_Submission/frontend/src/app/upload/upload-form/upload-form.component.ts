import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { environment } from '../../../environments/environment';
import { EncryptionService } from 'src/app/services/end-dec.service';

@Component({
  selector: 'app-upload-form',
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.scss']
})
export class UploadFormComponent implements OnInit {
  private postUrl = environment.POST_URL;
  private testUrl = 'https://storage.googleapis.com/strength-grader-upload';
  @Output() resId = new EventEmitter();
  public store = {
    positions: [
      { id: 0, value: 'Junior Software Engineer'},
      { id: 1, value: 'Mid-level Software Engineer'},
      { id: 2, value: 'Senior Software Engineer'},
      { id: 3, value: 'Junior Data Analyst'},
      { id: 4, value: 'Data Architect'},
    ]
  };
  @Output() step = new EventEmitter();

  constructor(private encryptionService: EncryptionService) { }

  ngOnInit() {
  }


  public uploadNotification(event: any): void {
    this.step.emit(event.file);
  }

  public getUrl(name): string {
    const encrypted = btoa(name.split('.')[0]);
    this.resId.emit(encrypted);
    return this.testUrl + `/${encrypted}.pdf`;
  }
}
