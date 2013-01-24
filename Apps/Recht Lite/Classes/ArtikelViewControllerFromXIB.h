//
//  ArtikelViewControllerFromXIB.h
//  Wetboek
//
//  Created by rabshakeh on 5/29/09 - 10:18 AM.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>


@interface ArtikelViewControllerFromXIB : UIViewController<UIGestureRecognizerDelegate> {
  NSString                 *artikel_id ;
  NSString                 *artikelbestand ;
  NSString                 *bookmark_titel ;
  NSString                 *bookmark_boek ;
  NSString                 *bookmark_artikel ;
  NSString                 *bookmark_subtitel ;
  NSString                 *databasePath ;
  IBOutlet UIBarButtonItem *bookmarkbtn ;
  IBOutlet UIBarButtonItem *bookmarksbtn ;
  IBOutlet UIBarButtonItem *backbtn ;
  IBOutlet UIBarButtonItem *forwardbtn ;
  IBOutlet UIWebView       *webView ;
  UIActivityIndicatorView  *progressIndicator ;
  BOOL                     first_load,
                           webviewrender ;
  int                      first, last ;
}

@property (retain, nonatomic) NSString                         *artikel_id ;
@property (retain, nonatomic) NSString                         *artikelbestand ;
@property (retain, nonatomic) UIBarButtonItem                  *backbtn ;
@property (retain, nonatomic) UIBarButtonItem                  *bookmarkbtn ;
@property (retain, nonatomic) UIBarButtonItem                  *bookmarksbtn ;
@property (retain, nonatomic) UIBarButtonItem                  *forwardbtn ;
@property (retain, nonatomic) NSString                         *bookmark_titel ;
@property (retain, nonatomic) NSString                         *bookmark_boek ;
@property (retain, nonatomic) NSString                         *bookmark_artikel ;
@property (retain, nonatomic) NSString                         *bookmark_subtitel ;
@property (retain, nonatomic) NSString                         *databasePath ;
@property  BOOL                                                webviewrender ;

@property (retain, nonatomic) IBOutlet UIWebView               *webView ;
@property (nonatomic, retain) IBOutlet UIActivityIndicatorView *progressIndicator ;

-(id)initWithText        : (NSString *)someText ;
-(IBAction)back          : (id)sender ;
-(IBAction)forward       : (id)sender ;
-(IBAction)popToHome     : (id)sender ;
-(IBAction)makeBookmark  : (id)sender ;
-(IBAction)showBookmarks : (id)sender ;
@end
