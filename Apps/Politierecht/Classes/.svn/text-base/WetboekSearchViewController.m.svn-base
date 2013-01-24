//
//  WetboekSearchViewController.m
//  WetboekSearch
//
//  Created by rabshakeh on 6/15/09 - 1:09 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "WetboekSearchViewController.h"
#import "Sqlite.h"
#import "TableViewFromDatabaseViewController.h"

@implementation WetboekSearchViewController

@synthesize myTableView ;
@synthesize searchBar ;
@synthesize progressIndicator ;
@synthesize currentSearchText ;
@synthesize myLock ;

// The designated initializer. Override to perform setup that is required before the view is loaded.
-(id) initWithNibName: (NSString *) nibNameOrNil bundle: (NSBundle *) nibBundleOrNil
{
  if (self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil]) {
    // Custom initialization
    search_items = [[NSMutableDictionary alloc] initWithCapacity:50] ;
    [progressIndicator hidesWhenStopped] ;
  }
  return(self) ;
}

-(void) reloadDataTableViewWetboek
{
  NSAutoreleasePool *autoreleasepool = [[NSAutoreleasePool alloc] init] ;

  if ([search_items count] == 0) {
    NSString            *targetresult = @"Geen resultaten" ;
    NSString            *stag         = [[NSString alloc] initWithFormat:@"%d", 0] ;
    NSMutableDictionary *tempdict     = [[NSMutableDictionary alloc] initWithCapacity:1] ;
    [tempdict setObject:targetresult forKey:@"text"] ;
    [search_items setObject:tempdict forKey:stag] ;
    [stag release] ;
    [tempdict release] ;
  }
  [self.myTableView reloadData] ;
  [progressIndicator stopAnimating] ;
  [autoreleasepool release] ;
}

-(NSDictionary *) addItemsToDict: (NSString *) query targetWord: (NSString *) targetword currentTag: (int) tag nextTable: (NSString *) nexttable
{
  Sqlite *sqlite = [[Sqlite alloc] init] ;

  [sqlite open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]] ;
  NSArray  *results    = [sqlite executeQueryCopy:query] ;
  NSString *itemsfound = [[NSString alloc] initWithFormat:@"%d", [results count]] ;
  NSString *stag ;

  if ([itemsfound intValue] > 0) {
    for (NSDictionary *resdict in results) {
      stag = [[NSString alloc] initWithFormat:@"%d", tag] ;
      NSString            *targetresult = [resdict objectForKey:targetword] ;
      NSMutableDictionary *tempdict     = [[NSMutableDictionary alloc] initWithCapacity:1] ;
      [tempdict setObject:[resdict objectForKey:@"id"] forKey:@"id"] ;
      [tempdict setObject:targetresult forKey:@"text"] ;
      [tempdict setObject:nexttable forKey:@"nexttable"] ;
      [search_items setObject:tempdict forKey:stag] ;
      [stag release] ;
      [tempdict release] ;
      tag += 1 ;
    }
  }
  stag = [[NSString alloc] initWithFormat:@"%d", tag] ;
  NSArray      *keys       = [NSArray arrayWithObjects:@"tag", @"itemsfound", nil] ;
  NSArray      *objects    = [NSArray arrayWithObjects:stag, itemsfound, nil] ;
  NSDictionary *dictionary = [NSDictionary dictionaryWithObjects:objects forKeys:keys] ;

  [results release] ;
  [sqlite release] ;
  [itemsfound release] ;
  [stag release] ;
  return(dictionary) ;
}

-(void) performSearch
{
  NSAutoreleasePool *autoreleasepool = [[NSAutoreleasePool alloc] init] ;

  [myLock lock] ;
  [search_items removeAllObjects] ;
  if ([self.currentSearchText length] > 0) {
    int      tag = 0 ;

    NSString *query = [[NSString alloc] initWithFormat:@"SELECT id, titel FROM wetboekhoofdstuk WHERE titel LIKE '%%%@%%' ORDER BY titel", self.currentSearchText] ;
    tag = [[[self addItemsToDict:query targetWord:@"titel" currentTag:tag nextTable:@"wetboek"] objectForKey:@"tag"] intValue] ;
    [query release] ;

    query = [[NSString alloc] initWithFormat:@"SELECT id, titel FROM wetboek WHERE afk LIKE '%%%@%%' AND volgende = 'hoofdstukken' ORDER BY titel", self.currentSearchText] ;
    NSDictionary *retdict = [self addItemsToDict:query targetWord:@"titel" currentTag:tag nextTable:@"hoofdstukken"] ;
    tag = [[retdict objectForKey:@"tag"] intValue] ;
    int          itemsfound = [[retdict objectForKey:@"itemsfound"] intValue] ;
    [query release] ;

    if (itemsfound == 0) {
      query = [[NSString alloc] initWithFormat:@"SELECT id, titel FROM wetboek WHERE titel LIKE '%%%@%%' AND volgende = 'hoofdstukken' ORDER BY titel", self.currentSearchText] ;
      tag   = [[[self addItemsToDict:query targetWord:@"titel" currentTag:tag nextTable:@"hoofdstukken"] objectForKey:@"tag"] intValue] ;
      [query release] ;
    }

    query = [[NSString alloc] initWithFormat:@"SELECT id, steekwoord FROM searchindex WHERE steekwoord LIKE '%@%%' ORDER BY steekwoord LIMIT 20 ", self.currentSearchText] ;
    [self addItemsToDict:query targetWord:@"steekwoord" currentTag:tag nextTable:@"herkomst"] ;
    [query release] ;
  }
  [self performSelectorOnMainThread:@selector(reloadDataTableViewWetboek) withObject:nil waitUntilDone:NO] ;
  [myLock unlock] ;
  [autoreleasepool release] ;
}

-(void) searchBarSearchButtonClicked: (UISearchBar *) searchBar2
{
  [progressIndicator startAnimating] ;
  [searchBar resignFirstResponder] ;
  self.currentSearchText = [searchBar2.text stringByTrimmingCharactersInSet:[NSCharacterSet whitespaceAndNewlineCharacterSet]] ;
  [NSThread detachNewThreadSelector:@selector(performSearch) toTarget:self withObject:nil] ;
}

-(void) searchBar: (UISearchBar *) aSearchBar textDidChange: (NSString *) searchText
{
}


/*
 * // Implement loadView to create a view hierarchy programmatically, without using a nib.
 * - (void)loadView {
 * }
 */

-(void) stop
{
  [self.navigationController popToRootViewControllerAnimated:YES] ;
}

// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
-(void) viewDidLoad
{
  [searchBar becomeFirstResponder] ;

  UIBarButtonItem *barButtonItem = [[UIBarButtonItem alloc] initWithImage:[UIImage imageNamed:@"home.png"] style:UIBarButtonItemStyleBordered target:self action:@selector(stop)] ;
  self.navigationItem.rightBarButtonItem = barButtonItem ;
  [barButtonItem release] ;

  [super viewDidLoad] ;
}

-(void) viewWillAppear: (BOOL) animated
{
  // Unselect the selected row if any
  NSIndexPath *selection = [self.myTableView indexPathForSelectedRow] ;

  if (selection) {
    [self.myTableView deselectRowAtIndexPath:selection animated:YES] ;
  }

  [super viewWillAppear:animated] ;
}


// Override to allow orientations other than the default portrait orientation.
-(BOOL) shouldAutorotateToInterfaceOrientation: (UIInterfaceOrientation) interfaceOrientation
{
  return(YES) ;
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

-(NSInteger) tableView: (UITableView *) tableView numberOfRowsInSection: (NSInteger) section
{
  return([search_items count]) ;
}

-(UITableViewCell *) tableView: (UITableView *) tableView cellForRowAtIndexPath: (NSIndexPath *) indexPath
{
  UITableViewCell *cell = [[[UITableViewCell alloc] initWithFrame:CGRectZero reuseIdentifier:nil] autorelease] ;

  NSString        *stag = [[NSString alloc] initWithFormat:@"%d", indexPath.row] ;

  cell.tag            = indexPath.row ;
  cell.textLabel.font = [UIFont fontWithName: @"Helvetica" size: 17.0] ;
  cell.selectionStyle = UITableViewCellSelectionStyleGray ;
  cell.textLabel.text = [[search_items objectForKey:stag] objectForKey:@"text"] ;
  NSComparisonResult compResult = [cell.textLabel.text compare:@"Geen resultaten"] ;
  if (compResult != NSOrderedSame) {
    cell.accessoryType = UITableViewCellAccessoryDisclosureIndicator ;
  }

  [stag release] ;
  return(cell) ;
}

-(void) tableView: (UITableView *) tableView didSelectRowAtIndexPath: (NSIndexPath *) indexPath
{
  UITableViewCell    *cell      = [tableView cellForRowAtIndexPath: indexPath] ;
  NSComparisonResult compResult = [cell.textLabel.text compare:@"Geen resultaten"] ;

  if (compResult == NSOrderedSame) {
    return ;
  }

  NSString *stag      = [[NSString alloc] initWithFormat:@"%d", cell.tag] ;
  NSString *nexttable = [[search_items objectForKey:stag] objectForKey:@"nexttable"] ;
  compResult = [nexttable compare:@"wetboek"] ;

  if (compResult == NSOrderedSame) {
    TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;
    tableViewFromDatabaseController.title        = @"Wetten" ;
    tableViewFromDatabaseController.backbutton   = tableViewFromDatabaseController.title ;
    tableViewFromDatabaseController.table_name   = @"wetboek" ;
    tableViewFromDatabaseController.next_table   = @"hoofdstukken" ;
    tableViewFromDatabaseController.currentID    = [[search_items objectForKey:stag] objectForKey:@"id"] ;
    tableViewFromDatabaseController.where_clause = [NSString stringWithFormat:@"where wetboekhoofdstuk_id=%@", [[search_items objectForKey:stag] objectForKey:@"id"]] ;
    [tableViewFromDatabaseController reload] ;
    [self.navigationController pushViewController:tableViewFromDatabaseController animated:YES] ;
    [tableViewFromDatabaseController release] ;
  }

  compResult = [nexttable compare:@"hoofdstukken"] ;
  if (compResult == NSOrderedSame) {
    TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;
    Sqlite                              *sqlite                          = [[Sqlite alloc] init] ;
    [sqlite open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]] ;
    NSString                            *query2  = [[NSString alloc] initWithFormat:@"select afk from wetboek where id='%@'", [[search_items objectForKey:stag] objectForKey:@"id"]] ;
    NSArray                             *results = [sqlite executeQueryCopy: query2] ;
    NSString                            *afk     = [NSString stringWithFormat:@"%@", [[results objectAtIndex:0] objectForKey:@"afk"]] ;
    [query2 release] ;
    [sqlite release] ;
    [results release] ;
    tableViewFromDatabaseController.title        = afk ;
    tableViewFromDatabaseController.backbutton   = tableViewFromDatabaseController.title ;
    tableViewFromDatabaseController.table_name   = @"hoofdstukken" ;
    tableViewFromDatabaseController.next_table   = @"artikel" ;
    tableViewFromDatabaseController.currentID    = [[search_items objectForKey:stag] objectForKey:@"id"] ;
    tableViewFromDatabaseController.where_clause = [NSString stringWithFormat:@"where wetboek_id=%@", [[search_items objectForKey:stag] objectForKey:@"id"]] ;
    [tableViewFromDatabaseController reload] ;
    [self.navigationController pushViewController:tableViewFromDatabaseController animated:YES] ;
    [tableViewFromDatabaseController release] ;
  }

  compResult = [nexttable compare:@"herkomst"] ;
  if (compResult == NSOrderedSame) {
    TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;
    tableViewFromDatabaseController.title        = cell.textLabel.text ;
    tableViewFromDatabaseController.backbutton   = tableViewFromDatabaseController.title ;
    tableViewFromDatabaseController.table_name   = @"herkomst" ;
    tableViewFromDatabaseController.next_table   = @"artikel" ;
    tableViewFromDatabaseController.where_clause = [NSString stringWithFormat:@"where searchindex_id=%@ order by titel, artikel", [[search_items objectForKey:stag] objectForKey:@"id"]] ;
    [tableViewFromDatabaseController reload] ;
    [self.navigationController pushViewController:tableViewFromDatabaseController animated:YES] ;
    [tableViewFromDatabaseController release] ;
  }

  [stag release] ;
}


@end



