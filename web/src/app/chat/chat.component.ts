import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  chatUrl: SafeResourceUrl;
  isChatVisible = false;

  constructor(private sanitizer: DomSanitizer) {
    this.chatUrl = '';
  }

  ngOnInit() {
    var url = environment.amazonQUrl;
    this.chatUrl = this.sanitizer.bypassSecurityTrustResourceUrl(url);
  }

  toggleChat() {
    this.isChatVisible = !this.isChatVisible;
  }
}
