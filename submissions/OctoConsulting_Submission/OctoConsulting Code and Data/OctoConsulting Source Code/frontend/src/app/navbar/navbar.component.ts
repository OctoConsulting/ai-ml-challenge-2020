import { Component, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class NavbarComponent implements OnInit {

  public store = {
    links: [
      {
        name: 'Upload',
        path: '/upload',
        isActive: true
      },
      // {
      //   name: 'Dashboard',
      //   path: '/dashboard',
      //   isActive: false
      // }
    ]
  };

  constructor() { }

  ngOnInit() {
  }

}
