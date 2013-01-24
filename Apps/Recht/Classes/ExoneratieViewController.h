//
//  ExoneratieViewController.h
//  Wetboek
//
//  Created by rabshakeh on 8/4/09 - 11:23 AM.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface ExoneratieViewController : UIViewController<UIWebViewDelegate, UIActionSheetDelegate> {
  IBOutlet UIWebView      *webView ;
  bool                    opensafari, openmail ;
  UIActivityIndicatorView *progressIndicator ;
}

@property (nonatomic, retain) IBOutlet UIActivityIndicatorView *progressIndicator ;
@property (retain, nonatomic) IBOutlet UIWebView               *webView ;

@end
