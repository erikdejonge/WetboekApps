//
//  ExoneratieViewController.m
//  Wetboek
//
//  Created by rabshakeh on 8/4/09 - 11:23 AM.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "ExoneratieViewController.h"

@implementation ExoneratieViewController

@synthesize webView;
@synthesize progressIndicator;

// The designated initializer.  Override if you create the controller programmatically and want to perform customization that is not appropriate for viewDidLoad.
-(id) initWithNibName: (NSString *) nibNameOrNil bundle: (NSBundle *) nibBundleOrNil
{
  if (self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil]) {
    // Custom initialization
    opensafari = NO;
    openmail   = NO;
    UIBarButtonItem *backBarButtonItem = [[UIBarButtonItem alloc] initWithTitle:@"Terug" style:UIBarButtonItemStyleBordered target:nil action:nil];
    self.navigationItem.backBarButtonItem = backBarButtonItem;
    [backBarButtonItem release];
  }
  return(self);
}

-(BOOL) webView: (UIWebView *) webView shouldStartLoadWithRequest: (NSURLRequest *) request navigationType: (UIWebViewNavigationType) navigationType
{
  NSString *url = [request.URL absoluteString];

  if (navigationType == UIWebViewNavigationTypeLinkClicked) {
    NSComparisonResult compResult = [url compare:@"http://www.active8.nl/"];
    if (compResult == NSOrderedSame) {
      UIAlertView *alertTest = [[UIAlertView alloc]
                                initWithTitle:@"Sociaalrecht 2011"
                                message:[NSString stringWithFormat:@"Afsluiten en naar de Active8 website gaan in Safari?"]
                                delegate:self
                                cancelButtonTitle:@"Annuleer"
                                otherButtonTitles:nil];
      [alertTest addButtonWithTitle:@"Open Safari"];
      [alertTest show];
      [alertTest autorelease];
      opensafari = YES;
      return(NO);
    }
    compResult = [url compare:@"mailto:info@active8.nl"];
    if (compResult == NSOrderedSame) {
      UIAlertView *alertTest = [[UIAlertView alloc]
                                initWithTitle:@"Sociaalrecht 2011"
                                message:[NSString stringWithFormat:@"Afsluiten en naar Mail gaan?"]
                                delegate:self
                                cancelButtonTitle:@"Annuleer"
                                otherButtonTitles:nil];
      [alertTest addButtonWithTitle:@"Open Mail"];
      [alertTest show];
      [alertTest autorelease];
      openmail = YES;
      return(NO);
    }
  }

  return(YES);
}

-(void) alertView: (UIAlertView *) alertView clickedButtonAtIndex: (NSInteger) buttonIndex
{
  if (buttonIndex == 1) {
    if (opensafari == YES) {
      [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://www.active8.nl"]];
    }
    if (openmail == YES) {
      [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"mailto:info@active8.nl?subject=Sociaalrecht_2011"]];
    }
  }
  opensafari = NO;
  openmail   = NO;
}

-(void) home
{
  [self.navigationController popToRootViewControllerAnimated:YES];
}

-(void) terug
{
  [self.navigationController popViewControllerAnimated:YES];
}

// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
-(void) viewDidLoad
{
  [self.webView loadHTMLString:@"<html><head><style> body {font-family: sans-serif; font-size: 12px;} table {font-family: sans-serif; font-size: 12px;} a {color: #ff6600;}</style></head><body>Een product van Active8 B.V.<br/><table border='0' cellspacing='0' cellpadding='1'><tr colspan='2'><td></td></tr><tr><td>Versie:</td><td>April 2011</td></tr><tr><td>Telefoon:</td><td>010-4144399</td></tr><tr><td>Email:</td><td><a href='mailto:info@active8.nl'>info@active8.nl</a></td></tr><tr><td>Website:</td><td><a href='http://www.active8.nl'>www.active8.nl</a></td></tr></body></html>" baseURL:nil];
  UIBarButtonItem *barButtonItem = [[UIBarButtonItem alloc] initWithImage:[UIImage imageNamed:@"home.png"] style:UIBarButtonItemStyleBordered target:self action:@selector(home)];
  self.navigationItem.rightBarButtonItem = barButtonItem;
  [barButtonItem release];

  UIBarButtonItem *backButton = [[[UIBarButtonItem alloc] initWithTitle:@"Terug" style:UIBarButtonItemStyleBordered target:self action:@selector(terug)] autorelease];
  self.navigationItem.leftBarButtonItem = backButton;

  [super viewDidLoad];
}

// Override to allow orientations other than the default portrait orientation.
-(BOOL) shouldAutorotateToInterfaceOrientation: (UIInterfaceOrientation) interfaceOrientation
{
  // Return YES for supported orientations
  return(NO);
}

-(void) didReceiveMemoryWarning
{
  // Releases the view if it doesn't have a superview.
  [super didReceiveMemoryWarning];

  // Release any cached data, images, etc that aren't in use.
}

-(void) viewDidUnload
{
  // Release any retained subviews of the main view.
  // e.g. self.myOutlet = nil;
}

-(void) dealloc
{
  [super dealloc];
}


-(void) webViewDidFinishLoad: (UIWebView *) webView
{
  [progressIndicator stopAnimating];
}

-(void) webViewDidStartLoad: (UIWebView *) webView
{
  [progressIndicator startAnimating];
}

@end
