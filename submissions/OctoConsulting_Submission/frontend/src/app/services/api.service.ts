import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { environment } from '../../environments/environment';
import { Observable, throwError } from 'rxjs';

@Injectable()
export class APIService {
    private baseUrl = environment.API_GATEWAY;
    constructor(private httpClient: HttpClient) { }

    public pollResults(resId: string): Observable<any> {
        const queryParams = {
            uuid: resId
        };

        return this.httpClient.get(this.baseUrl, {params: queryParams})
                .pipe(
                    map ( response => {
                        try {
                            return response;
                        } catch (e) {
                            throwError(e);
                        }
                    })
                );
    }
}
