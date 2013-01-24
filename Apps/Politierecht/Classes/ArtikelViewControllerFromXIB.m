//
//  ArtikelViewControllerFromXIB.m
//  Wetboek
//
//  Created by rabshakeh on 5/29/09 - 10:18 AM.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//
#import <QuartzCore/CAAnimation.h>
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "Sqlite.h"
#import "WetboekSearchViewController.h"

@implementation ArtikelViewControllerFromXIB

@synthesize artikel_id ;
@synthesize artikelbestand ;
@synthesize webView ;
@synthesize backbtn ;
@synthesize forwardbtn ;
@synthesize progressIndicator ;
@synthesize bookmark_titel ;
@synthesize bookmark_boek ;
@synthesize bookmark_artikel ;
@synthesize bookmark_subtitel ;
@synthesize databasePath ;
@synthesize bookmarkbtn ;
@synthesize bookmarksbtn ;
@synthesize webviewrender ;

-(id) initWithText: (NSString *) text
{
  if (self = [self initWithNibName:@"ArtikelViewControllerFromXIB" bundle:nil]) {
    self.artikel_id = text ;
    webviewrender   = NO ;
    first           = last = 1 ;
    if (self = [self init]) {
    }
  }
  return(self) ;
}

-(void) checkAndCreateDatabase
{
  NSString *databaseName  = @"bookmarks.db" ;
  NSArray  *documentPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) ;
  NSString *documentsDir  = [documentPaths objectAtIndex:0] ;

  self.databasePath = [documentsDir stringByAppendingPathComponent:databaseName] ;
  Sqlite   *sqlite = [[Sqlite alloc] init] ;
  [sqlite open: self.databasePath] ;
  NSString *query   = @"CREATE TABLE IF NOT EXISTS bookmarks(id INTEGER PRIMARY KEY, titel character varying(255) NOT NULL, boek character varying(255) NOT NULL, artikel integer NOT NULL, subtitel character varying(255) NOT NULL)" ;
  NSArray  *results = [sqlite executeQueryCopy:query] ;
  [results release] ;
  [query release] ;
  [sqlite commit] ;
  [sqlite dealloc] ;
}

-(void) storeBookMark
{
  self.bookmarkbtn.enabled = NO ;
  [self checkAndCreateDatabase] ;
  Sqlite *sqlite = [[Sqlite alloc] init] ;
  [sqlite open: self.databasePath] ;

  NSMutableString *lbookmark_titel    = [self.bookmark_titel mutableCopy] ;
  NSMutableString *lbookmark_boek     = [self.bookmark_boek mutableCopy] ;
  NSMutableString *lbookmark_artikel  = [self.bookmark_artikel mutableCopy] ;
  NSMutableString *lbookmark_subtitel = [self.bookmark_subtitel mutableCopy] ;

  [lbookmark_titel replaceOccurrencesOfString:@"'" withString:@"''" options:NSLiteralSearch range:NSMakeRange(0, [lbookmark_titel length])] ;
  [lbookmark_boek replaceOccurrencesOfString:@"'" withString:@"''" options:NSLiteralSearch range:NSMakeRange(0, [lbookmark_boek length])] ;
  [lbookmark_artikel replaceOccurrencesOfString:@"'" withString:@"''" options:NSLiteralSearch range:NSMakeRange(0, [lbookmark_artikel length])] ;
  [lbookmark_subtitel replaceOccurrencesOfString:@"'" withString:@"''" options:NSLiteralSearch range:NSMakeRange(0, [lbookmark_subtitel length])] ;

  NSString *query_art = [[NSString alloc] initWithFormat:@"INSERT INTO bookmarks VALUES (null, '%@', '%@', '%d', '%@');", lbookmark_titel, lbookmark_boek, [lbookmark_artikel integerValue], lbookmark_subtitel] ;
  NSArray  *results   = [sqlite executeQueryCopy:query_art] ;

  [results release] ;
  [sqlite commit] ;
  [query_art release] ;
  [lbookmark_titel release] ;
  [lbookmark_boek release] ;
  [lbookmark_artikel release] ;
  [lbookmark_subtitel release] ;

  [sqlite dealloc] ;
  self.bookmarksbtn.enabled = YES ;
}

-(IBAction) makeBookmark: (id) sender
{
  if (self.webviewrender == YES) {
    Sqlite   *sqlite        = [[Sqlite alloc] init] ;
    Sqlite   *sqlite_wetten = [[Sqlite alloc] init] ;

    NSString *query_art = [[NSString alloc] initWithFormat:@"select hoofdstuk_id, titel, tekst, first, last from artikel"] ;

    self.bookmark_artikel  = self.artikel_id ;
    self.bookmark_boek     = self.artikelbestand ;
    self.bookmark_subtitel = @"Tekst" ;


    [sqlite open:[[NSBundle mainBundle] pathForResource:self.artikelbestand ofType:@"db"]] ;
    NSArray *results = [sqlite executeQueryCopy:query_art] ;
    [query_art release] ;
    if ([results count] > 0) {
      self.bookmark_titel = [[results objectAtIndex:0] objectForKey:@"titel"] ;
    }

    [sqlite dealloc] ;
    [sqlite_wetten dealloc] ;
    [results release] ;
  }
  else{
    Sqlite   *sqlite        = [[Sqlite alloc] init] ;
    Sqlite   *sqlite_wetten = [[Sqlite alloc] init] ;

    NSString *query_art = [[NSString alloc] initWithFormat:@"select hoofdstuk_id, titel, tekst, first, last from artikel where id='%d'", [self.artikel_id integerValue]] ;

    self.bookmark_artikel = self.artikel_id ;
    [sqlite open:[[NSBundle mainBundle] pathForResource:self.artikelbestand ofType:@"db"]] ;
    NSArray *results = [sqlite executeQueryCopy:query_art] ;
    [query_art release] ;
    if ([results count] > 0) {
      [sqlite_wetten open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]] ;
      self.bookmark_subtitel = [[results objectAtIndex:0] objectForKey:@"titel"] ;
      NSString *query_hfst = [[NSString alloc] initWithFormat:@"SELECT * FROM hoofdstukken WHERE id =  '%d'", [[[results objectAtIndex:0] objectForKey:@"hoofdstuk_id"] integerValue]] ;
      NSArray  *r2         = [sqlite_wetten executeQueryCopy:query_hfst] ;
      [query_hfst release] ;
      if ([r2 count] > 0) {
        self.bookmark_boek = [[r2 objectAtIndex:0] objectForKey:@"artikelbestand"] ;
        NSString *query_wb = [[NSString alloc] initWithFormat:@"SELECT * FROM wetboek WHERE id =  '%d'", [[[r2 objectAtIndex:0] objectForKey:@"wetboek_id"] integerValue]] ;
        NSArray  *r3       = [sqlite_wetten executeQueryCopy:query_wb] ;
        [query_wb release] ;
        if ([r3 count] > 0) {
          self.bookmark_titel = [[r3 objectAtIndex:0] objectForKey:@"titel"] ;
        }
        [r3 release] ;
      }
      [r2 release] ;
    }

    [sqlite dealloc] ;
    [sqlite_wetten dealloc] ;
    [results release] ;
  }
  [self storeBookMark] ;
}

-(id) initWithNibName: (NSString *) nibNameOrNil bundle: (NSBundle *) nibBundleOrNil
{
  if (self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil]) {
    [progressIndicator hidesWhenStopped] ;
    first_load = YES ;
  }
  return(self) ;
}

-(void) setText
{
  [self checkAndCreateDatabase] ;
  Sqlite   *sqlite = [[Sqlite alloc] init] ;
  [sqlite open: self.databasePath] ;
  NSString *query   = [[NSString alloc] initWithFormat:@"select id from bookmarks where artikel='%@' and boek='%@'", self.artikel_id, self.artikelbestand] ;
  NSArray  *results = [sqlite executeQueryCopy:query] ;
  if ([results count] > 0) {
    self.bookmarkbtn.enabled = NO ;
  }
  [query release] ;
  [results release] ;
  query   = @"SELECT id FROM bookmarks" ;
  results = [sqlite executeQueryCopy:query] ;
  if ([results count] > 0) {
    self.bookmarksbtn.enabled = YES ;
  }
  else{
    self.bookmarksbtn.enabled = NO ;
  }
  [results release] ;
  [query release] ;
  if (webviewrender == YES) {
    query = [[NSString alloc] initWithFormat:@"select hoofdstuk_id, titel, tekst, first, last from artikel"] ;
  }
  else{
    query = [[NSString alloc] initWithFormat:@"select hoofdstuk_id, titel, tekst, first, last from artikel where id='%d'", [self.artikel_id integerValue]] ;
  }
  [sqlite open:[[NSBundle mainBundle] pathForResource:self.artikelbestand ofType:@"db"]] ;
  results = [sqlite executeQueryCopy:query] ;
  if ([results count] > 0) {
    [self.webView loadHTMLString:[[results objectAtIndex:0] objectForKey:@"tekst"] baseURL:nil] ;
    self.title              = [[results objectAtIndex:0] objectForKey:@"titel"] ;
    self.backbtn.enabled    = YES ;
    self.forwardbtn.enabled = YES ;
    NSString           *str_first = [[results objectAtIndex:0] objectForKey:@"first"] ;
    first = [str_first integerValue] ;
    NSComparisonResult compResult = [str_first compare:@"1"] ;
    if (compResult == NSOrderedSame) {
      self.backbtn.enabled = NO ;
    }
    NSString *str_last = [[results objectAtIndex:0] objectForKey:@"last"] ;
    last       = [str_last integerValue] ;
    compResult = [str_last compare:@"1"] ;
    if (compResult == NSOrderedSame) {
      self.forwardbtn.enabled = NO ;
    }
  }
  if (webviewrender == YES) {
    self.backbtn.enabled    = NO ;
    self.forwardbtn.enabled = NO ;
  }
  [sqlite dealloc] ;
  [results release] ;
  [query release] ;
}

-(IBAction) back: (id) sender
{
  self.bookmarkbtn.enabled = YES ;
  self.artikel_id          = [[NSString alloc] initWithFormat:@"%d", [self.artikel_id intValue] - 1] ;
  [self setText] ;
}

-(IBAction) forward: (id) sender
{
  self.bookmarkbtn.enabled = YES ;
  self.artikel_id          = [[NSString alloc] initWithFormat:@"%d", [self.artikel_id intValue] + 1] ;
  [self setText] ;
}

// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
-(void) viewDidLoad
{
  [super viewDidLoad] ;
  UISwipeGestureRecognizer *swipeRight = [[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(swipeRightAction:)] ;
  swipeRight.direction = UISwipeGestureRecognizerDirectionRight ;
  swipeRight.delegate  = self ;
  [webView addGestureRecognizer:swipeRight] ;
  [swipeRight release] ;

  UISwipeGestureRecognizer *swipeLeft = [[UISwipeGestureRecognizer alloc] initWithTarget:self action:@selector(swipeLeftAction:)] ;
  swipeLeft.direction = UISwipeGestureRecognizerDirectionLeft ;
  swipeLeft.delegate  = self ;
  [webView addGestureRecognizer:swipeLeft] ;
  [swipeLeft release] ;

  UIBarButtonItem *barButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemSearch target:self action:@selector(search:)] ;

  self.navigationItem.rightBarButtonItem = barButtonItem ;
  [barButtonItem release] ;

  [self setText] ;
}

-(BOOL) gestureRecognizer: (UIGestureRecognizer *) gestureRecognizer shouldRecognizeSimultaneouslyWithGestureRecognizer: (UIGestureRecognizer *) otherGestureRecognizer
{
  return(YES) ;
}

-(void) swipeRightAction: (id) ignored
{
  if (1 == first) {
    return ;
  }
  //add Function
  self.bookmarkbtn.enabled = YES ;
  self.artikel_id          = [[NSString alloc] initWithFormat:@"%d", [self.artikel_id intValue] - 1] ;

  [self setText] ;

  CATransition *myTransition = [CATransition animation] ;
  myTransition.timingFunction = UIViewAnimationCurveEaseInOut ;
  myTransition.type           = kCATransitionPush ;
  myTransition.subtype        = kCATransitionFromLeft ;
  [self.webView.layer addAnimation:myTransition forKey: nil] ;
}

-(void) swipeLeftAction: (id) ignored
{
  if (1 == last) {
    return ;
  }
  //add Function
  self.bookmarkbtn.enabled = YES ;
  self.artikel_id          = [[NSString alloc] initWithFormat:@"%d", [self.artikel_id intValue] + 1] ;
  [self setText] ;

  CATransition *myTransition = [CATransition animation] ;
  myTransition.timingFunction = UIViewAnimationCurveEaseInOut ;
  myTransition.type           = kCATransitionPush ;
  myTransition.subtype        = kCATransitionFromRight ;
  [self.webView.layer addAnimation:myTransition forKey: nil] ;
}

-(void) search: (id) sender
{
  WetboekSearchViewController *searchViewController = [[WetboekSearchViewController alloc] init] ;

  searchViewController.title = @"Zoeken" ;
  [self.navigationController pushViewController:searchViewController animated:YES] ;
  [searchViewController release] ;
}

// Override to allow orientations other than the default portrait orientation.
-(BOOL) shouldAutorotateToInterfaceOrientation: (UIInterfaceOrientation) interfaceOrientation
{
  // Return YES for supported orientations
  return(YES) ;
}

-(void) didRotateFromInterfaceOrientation: (UIInterfaceOrientation) fromInterfaceOrientation
{
  [self setText] ;
}

-(void) didReceiveMemoryWarning
{
  // Releases the view if it doesn't have a superview.
  [super didReceiveMemoryWarning] ;

  // Release any cached data, images, etc that aren't in use.
}

-(void) viewDidUnload
{
  // Release any retained subviews of the main view.
  // e.g. self.myOutlet = nil;
}

-(void) dealloc
{
  [super dealloc] ;
}

-(void) webViewDidFinishLoad: (UIWebView *) webView
{
  //backButton.enabled = [webView canGoBack];
  //forwardButton.enabled = [webView canGoForward];
  //statusLabel.text = @"";
  [progressIndicator stopAnimating] ;
}

-(void) webViewDidStartLoad: (UIWebView *) webView
{
  if (first_load == YES) {
    [progressIndicator startAnimating] ;
    first_load = NO ;
  }
}

-(IBAction) popToHome: (id) sender
{
  [self.navigationController popToRootViewControllerAnimated:YES] ;
}

-(IBAction) showBookmarks: (id) sender
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;

  tableViewFromDatabaseController.title        = @"Referenties" ;
  tableViewFromDatabaseController.backbutton   = self.title ;
  tableViewFromDatabaseController.table_name   = @"bookmarks" ;
  tableViewFromDatabaseController.next_table   = @"artikel" ;
  tableViewFromDatabaseController.where_clause = @"" ;
  [tableViewFromDatabaseController reload] ;
  [self.navigationController pushViewController:tableViewFromDatabaseController animated:YES] ;
  [tableViewFromDatabaseController release] ;
}

@end

