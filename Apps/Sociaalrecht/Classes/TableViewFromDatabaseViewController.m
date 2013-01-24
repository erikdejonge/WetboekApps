//
//  TableViewFromDatabaseViewController.m
//  TableViewFromDatabase
//
//  Created by rabshakeh on 6/22/09 - 11:40 AM.
//  Copyright __MyCompanyName__ 2009. All rights reserved.
//

#import "Sqlite.h"
#import "WetboekSearchViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "TableViewFromDatabaseViewController.h"
#import "CustomCell.h"
#import "CustomCellLong.h"
#import "ExoneratieViewController.h"
#import <QuartzCore/CAAnimation.h>

@implementation TableViewFromDatabaseViewController

@synthesize table_name;
@synthesize table_id;
@synthesize where_clause;
@synthesize query;
@synthesize next_table;
@synthesize artikelbestand;
@synthesize bevatartikelen;
@synthesize backbutton;
@synthesize bookmarkbtn;
@synthesize myTableView;
@synthesize currentIndexPath;
@synthesize myLock;
@synthesize exoneratieBtn;
@synthesize backbtn;
@synthesize forwardbtn;
@synthesize homebtn;
@synthesize currentID;
@synthesize afkorting;
@synthesize tag;

// todo: deselect cell als je terug 'popt'

// The designated initializer. Override to perform setup that is required before the view is loaded.
-(id) initWithNibName: (NSString *) nibNameOrNil bundle: (NSBundle *) nibBundleOrNil
{
  if (self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil]) {
    // Custom initialization
    sections            = [[NSMutableArray alloc] init];
    section_names       = [[NSMutableArray alloc] init];
    rows                = [[NSMutableArray alloc] init];
    self.query          = @"";
    self.table_name     = @"table_name not set!!";
    self.table_id       = @"-777";
    self.where_clause   = @"";
    self.next_table     = @"next table is never set!!";
    self.artikelbestand = @"None";
    self.backbutton     = @"Terug";
    self.afkorting      = @"Terug";
    //self.currentID = @"-777";
    changedOrientation = NO;
  }
  return(self);
}

-(void) startEditing
{
  [self.myTableView setEditing: YES animated: YES];

  self.navigationItem.rightBarButtonItem = [[[UIBarButtonItem alloc]
                                             initWithBarButtonSystemItem: UIBarButtonSystemItemDone
                                             target: self
                                             action: @selector(stopEditing)] autorelease];
}

-(void) stopEditing
{
  [self.myTableView setEditing: NO animated: YES];

  self.navigationItem.rightBarButtonItem = [[[UIBarButtonItem alloc]
                                             initWithBarButtonSystemItem: UIBarButtonSystemItemEdit
                                             target: self
                                             action: @selector(startEditing)] autorelease];
}

-(void) reload
{
  [sections removeAllObjects];
  [section_names removeAllObjects];
  [rows removeAllObjects];

  Sqlite *sqlite = [[Sqlite alloc] init];

  if ([self.artikelbestand compare:@"None"] == NSOrderedSame) {
    [sqlite open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]];
  }
  else{
    [sqlite open:[[NSBundle mainBundle] pathForResource:self.artikelbestand ofType:@"db"]];
  }

  if ([self.table_name compare:@"hoofdstukken"] == NSOrderedSame) {
    query = @"-777";
    if ([self.table_name compare:@"hoofdstukken"] == NSOrderedSame) {
      query = [[NSString alloc] initWithFormat:@"select titel, afk from wetboek where id='%d'", [self.currentID integerValue]];
    }

    if ([query compare:@"-777"] != NSOrderedSame) {
      NSArray *results = [sqlite executeQueryCopy:query];

      if ([results count] > 0) {
        self.title = [[results objectAtIndex:0] objectForKey:@"titel"];
        UIBarButtonItem *newBackButton = [[UIBarButtonItem alloc] initWithTitle:[[results objectAtIndex:0] objectForKey:@"afk"] style: UIBarButtonItemStyleBordered target: nil action: nil];
        [[self navigationItem] setBackBarButtonItem: newBackButton];
        [newBackButton release];
      }
      [results release];
    }

    query = [[NSString alloc] initWithFormat:@"select id, hoofdstuk_id, titel, subtitel, volgende, bevatartikelen, artikelbestand from %@ %@ order by sequence", self.table_name, self.where_clause];

    NSArray *results = [sqlite executeQueryCopy: query];

    for (NSDictionary *dictionary in results) {
      NSString           *strbevatarts   = [dictionary objectForKey:@"bevatartikelen"];
      NSComparisonResult bbevatartikelen = [strbevatarts compare:@"NO"];
      if (bbevatartikelen == NSOrderedSame) {
        NSMutableArray *celldata = [[NSMutableArray alloc] init];
        [sections addObject:celldata];
        [celldata release];
        [section_names addObject:[dictionary objectForKey:@"titel"]];
      }
      else{
        if (0 ==[sections count]) {
          NSMutableArray *celldata = [[NSMutableArray alloc] init];
          [sections addObject:celldata];
          if ([section_names count] == 0) {
            [section_names addObject:@"xxxxxxxx"];
          }
          else{
            [section_names addObject:[dictionary objectForKey:@"titel"]];
          }
          [celldata release];
        }
        [[sections lastObject] addObject:dictionary];
      }
    }
    [results release];
  }
  else{
    if ([self.table_name compare:@"herkomst"] != NSOrderedSame &&
        [self.table_name compare:@"bookmarks"] != NSOrderedSame) {
      query = @"-777";
      if ([self.table_name compare:@"wetboek"] == NSOrderedSame) {
        query = [[NSString alloc] initWithFormat:@"select titel from wetboekhoofdstuk where id='%d'", [self.currentID integerValue]];
      }

      if ([query compare:@"-777"] != NSOrderedSame) {
        NSArray *results = [sqlite executeQueryCopy:query];
        if ([results count] > 0) {
          [section_names addObject:[[results objectAtIndex:0] objectForKey:@"titel"]];
        }
        [results release];
      }
      if ([self.table_name compare:@"artikel"] == NSOrderedSame) {
        query = [[NSString alloc] initWithFormat:@"select id, titel, teaser, volgende from %@ %@ order by sequence", self.table_name, self.where_clause];
      }
      else{
      query = [[NSString alloc] initWithFormat:@"select id, titel, volgende from %@ %@ order by sequence", self.table_name, self.where_clause];
      }
      NSArray *results = [sqlite executeQueryCopy: query];
      for (NSDictionary *dictionary in results) {
        if (0 ==[sections count]) {
          NSMutableArray *celldata = [[NSMutableArray alloc] init];
          [celldata addObject:dictionary];
          [sections addObject:celldata];
          [celldata release];
        }
        else{
          [[sections lastObject] addObject:dictionary];
        }
        [rows addObject:dictionary];
      }
      [results release];
    }
  }

  if ([self.table_name compare:@"herkomst"] == NSOrderedSame) {
    query = [[NSString alloc] initWithFormat:@"select * from herkomst %@ ", self.where_clause];
    NSArray *results = [sqlite executeQueryCopy: query];
    for (NSDictionary *dictionary in results) {
      if (0 ==[sections count]) {
        NSMutableArray *celldata = [[NSMutableArray alloc] init];
        [celldata addObject:dictionary];
        [sections addObject:celldata];
        [celldata release];
      }
      else{
        [[sections lastObject] addObject:dictionary];
      }
      [rows addObject:dictionary];
    }
    [results release];
  }

  if ([self.table_name compare:@"bookmarks"] == NSOrderedSame) {
    query = [[NSString alloc] initWithFormat:@"select * from bookmarks %@ ", self.where_clause];
    NSString *databaseName  = @"bookmarks.db";
    NSArray  *documentPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDir  = [documentPaths objectAtIndex:0];
    NSString *databasePath  = [documentsDir stringByAppendingPathComponent:databaseName];
    Sqlite   *sqlitebm      = [[Sqlite alloc] init];
    [sqlitebm open: databasePath];
    NSArray  *results = [sqlitebm executeQueryCopy: query];
    for (NSDictionary *dictionary in results) {
      if (0 ==[sections count]) {
        NSMutableArray *celldata = [[NSMutableArray alloc] init];
        [celldata addObject:dictionary];
        [sections addObject:celldata];
        [celldata release];
      }
      else{
        [[sections lastObject] addObject:dictionary];
      }
      [rows addObject:dictionary];
    }
    [results release];
    [sqlitebm release];
  }

  [sqlite release];
}

-(NSInteger) numberOfSectionsInTableView: (UITableView *) tableView
{
  int sc = [sections count];

  return(sc);
}

-(NSInteger) tableView: (UITableView *) tableView numberOfRowsInSection: (NSInteger) section
{
  int count = [[sections objectAtIndex:section] count];

  return(count);
}


-(UITableViewCell *) tableView: (UITableView *) tableView cellForRowAtIndexPath: (NSIndexPath *) indexPath
{
  NSArray            *rowsarray = [sections objectAtIndex: indexPath.section] ;
  NSDictionary       *rowdicts  = [rowsarray objectAtIndex:indexPath.row] ;
  UITableViewCell    *cell      = nil ;

  NSComparisonResult compResult  = [self.next_table compare:@"artikel"] ;
  NSComparisonResult compResult2 = [self.table_name compare:@"herkomst"] ;

  if (compResult == NSOrderedSame || compResult2 == NSOrderedSame) {
    NSString *titel = [rowdicts objectForKey:@"titel"] ;
    compResult = [titel compare:@"Alle artikelen"] ;
    if (compResult == NSOrderedSame) {
      cell                = [tableView dequeueReusableCellWithIdentifier:@"enkel"] ;
      if (nil == cell) {
        cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"enkel"] autorelease] ;
      }
      cell.textLabel.font = [UIFont fontWithName: @"Helvetica" size: 17.0] ;
      cell.textLabel.text = [rowdicts objectForKey:@"subtitel"] ;
    }
    else{
      cell                      = [tableView dequeueReusableCellWithIdentifier:@"dubbel"] ;
      if (nil == cell) {
        cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"dubbel"] autorelease] ;
      }
      cell.textLabel.font       = [UIFont fontWithName: @"Helvetica" size: 17.0] ;
      cell.detailTextLabel.font = [UIFont fontWithName: @"Helvetica" size: 13.0] ;
      cell.textLabel.text       = titel ;
      cell.detailTextLabel.text = [rowdicts objectForKey:@"subtitel"] ;
    }
  }
  else{
    if ([self.next_table compare:@"NoneShowArtikel"] == NSOrderedSame) {
      cell                      = [tableView dequeueReusableCellWithIdentifier:@"dubbel"] ;
      if (nil == cell) {
        cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"dubbel"] autorelease] ;
      }
      cell.textLabel.font       = [UIFont fontWithName: @"Helvetica" size: 17.0] ;
      cell.detailTextLabel.font = [UIFont fontWithName: @"Helvetica" size: 13.0] ;

      cell.textLabel.text       = [rowdicts objectForKey:@"titel"] ;
      cell.detailTextLabel.text = [rowdicts objectForKey:@"teaser"] ;
    }
    else {
      cell                = [tableView dequeueReusableCellWithIdentifier:@"enkel"] ;
      if (nil == cell) {
        cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:@"enkel"] autorelease] ;
      }
      cell.textLabel.font = [UIFont fontWithName: @"Helvetica" size: 17.0] ;

      cell.textLabel.text = [rowdicts objectForKey:@"titel"] ;
    }
  }

  cell.selectionStyle = UITableViewCellSelectionStyleGray ;
  cell.accessoryType  = UITableViewCellAccessoryDisclosureIndicator ;
  cell.tag            = [[rowdicts objectForKey:@"id"] intValue] ;
  return(cell) ;
}


/*
-(UITableViewCell *) tableView: (UITableView *) tableView cellForRowAtIndexPath: (NSIndexPath *) indexPath
{
  NSArray             *rowsarray = [sections objectAtIndex: indexPath.section];
  NSDictionary        *rowdicts  = [rowsarray objectAtIndex:indexPath.row];
  NSString            *CellIdentifier;
  UIDeviceOrientation orient = [UIDevice currentDevice].orientation;

  if (orient == UIDeviceOrientationLandscapeLeft || orient == UIDeviceOrientationLandscapeRight) {
    CellIdentifier = @"CustomCellLong";
    CustomCellLong *cell = (CustomCellLong *)[tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (changedOrientation) {
      cell = nil;
    }
    if (cell == nil) {
      NSArray *topLevelObjects = [[NSBundle mainBundle] loadNibNamed:CellIdentifier owner:self options:nil];
      for (id currentObject in topLevelObjects) {
        if ([currentObject isKindOfClass:[UITableViewCell class]]) {
          cell = (CustomCellLong *)currentObject;
          break;
        }
      }
    }

    NSComparisonResult compResult  = [self.next_table compare:@"artikel"];                      // hoofdstukken
    NSComparisonResult compResult2 = [self.table_name compare:@"herkomst"];
    if (compResult == NSOrderedSame || compResult2 == NSOrderedSame) {
      NSString *titel = [rowdicts objectForKey:@"titel"];
      compResult = [titel compare:@"Alle artikelen"];
      if (compResult == NSOrderedSame) {
        cell.midtitel.text = [rowdicts objectForKey:@"subtitel"];
        cell.titel.text    = @"";
        cell.subtitel.text = @"";
      }
      else{
        cell.midtitel.text = @"";
        cell.titel.text    = titel;
        cell.subtitel.text = [rowdicts objectForKey:@"subtitel"];
      }
    }
    else{
      cell.midtitel.text = [rowdicts objectForKey:@"titel"];
      cell.titel.text    = @"";
      cell.subtitel.text = @"";
    }
    cell.selectionStyle = UITableViewCellSelectionStyleGray;
    cell.accessoryType  = UITableViewCellAccessoryDisclosureIndicator;
    cell.tag            = [[rowdicts objectForKey:@"id"] intValue];
    return(cell);
  }

  else{
    CellIdentifier = @"CustomCell";
    CustomCell *cell = (CustomCell *)[tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (changedOrientation) {
      cell = nil;
    }
    if (cell == nil) {
      NSArray *topLevelObjects = [[NSBundle mainBundle] loadNibNamed:CellIdentifier owner:self options:nil];
      for (id currentObject in topLevelObjects) {
        if ([currentObject isKindOfClass:[UITableViewCell class]]) {
          cell = (CustomCell *)currentObject;
          break;
        }
      }
    }

    NSComparisonResult compResult  = [self.next_table compare:@"artikel"];
    NSComparisonResult compResult2 = [self.table_name compare:@"herkomst"];
    if (compResult == NSOrderedSame || compResult2 == NSOrderedSame) {
      NSString *titel = [rowdicts objectForKey:@"titel"];
      compResult = [titel compare:@"Alle artikelen"];
      if (compResult == NSOrderedSame) {
        cell.midtitel.text = [rowdicts objectForKey:@"subtitel"];
        cell.titel.text    = @"";
        cell.subtitel.text = @"";
      }
      else{
        cell.midtitel.text = @"";
        cell.titel.text    = titel;
        cell.subtitel.text = [rowdicts objectForKey:@"subtitel"];
      }
    }
    else{
      if ([self.next_table compare:@"NoneShowArtikel"] == NSOrderedSame) {
        cell.midtitel.text = @"";
        cell.titel.text    = [rowdicts objectForKey:@"titel"];
        cell.subtitel.text = [rowdicts objectForKey:@"teaser"];
      }
      else {
      cell.midtitel.text = [rowdicts objectForKey:@"titel"];
      cell.titel.text    = @"";
      cell.subtitel.text = @"";
    }
    }

    cell.selectionStyle = UITableViewCellSelectionStyleGray;
    cell.accessoryType  = UITableViewCellAccessoryDisclosureIndicator;
    cell.tag            = [[rowdicts objectForKey:@"id"] intValue];
    return(cell);
  }
   }*/

-(void) selectRowThreaded
{
  [self.myTableView selectRowAtIndexPath:self.currentIndexPath animated:NO scrollPosition:UITableViewScrollPositionNone];
}

-(NSIndexPath *) tableView: (UITableView *) tableView willSelectRowAtIndexPath: (NSIndexPath *) indexPath
{
  self.currentIndexPath = indexPath;
  [NSThread detachNewThreadSelector:@selector(selectRowThreaded) toTarget:self withObject:nil];

  return(indexPath);
}

-(void) pushToNextScreen
{
  UITableViewCell *cell = [self.myTableView cellForRowAtIndexPath: self.currentIndexPath];

  self.tag = [[NSString alloc] initWithFormat:@"%d", cell.tag];

  if ([self.table_name compare:@"herkomst"] == NSOrderedSame) {
    NSArray      *rowsarray = [sections objectAtIndex: self.currentIndexPath.section];
    NSDictionary *rowdicts  = [rowsarray objectAtIndex:self.currentIndexPath.row];
    self.artikelbestand = [rowdicts objectForKey:@"boek"];
    self.next_table     = @"NoneShowArtikel";
    self.tag            = [rowdicts objectForKey:@"artikel"];
    ArtikelViewControllerFromXIB *artikelViewController = [[ArtikelViewControllerFromXIB alloc] initWithText:self.tag];
    artikelViewController.artikelbestand = self.artikelbestand;
    if ([@"Tekst" compare:[rowdicts objectForKey:@"subtitel"]] == NSOrderedSame) {
      artikelViewController.webviewrender = YES;
    }
    [self.navigationController pushViewController:artikelViewController animated:YES];
    [artikelViewController release];
    return;
  }

  if ([self.table_name compare:@"bookmarks"] == NSOrderedSame) {
    NSString *databaseName  = @"bookmarks.db";
    NSArray  *documentPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *documentsDir  = [documentPaths objectAtIndex:0];
    NSString *databasePath  = [documentsDir stringByAppendingPathComponent:databaseName];
    Sqlite   *sqlite        = [[Sqlite alloc] init];
    [sqlite open: databasePath];
    NSString *query2  = [[NSString alloc] initWithFormat:@"select boek, subtitel, artikel from bookmarks where id='%d'", cell.tag];
    NSArray  *results = [sqlite executeQueryCopy:query2];
    if ([results count] > 0) {
      self.artikelbestand = [[results objectAtIndex:0] objectForKey:@"boek"];
      self.tag            = [[results objectAtIndex:0] objectForKey:@"artikel"];

      if ([@"Tekst" compare:[[results objectAtIndex:0] objectForKey:@"subtitel"]] == NSOrderedSame) {
        ArtikelViewControllerFromXIB *artikelViewController = [[ArtikelViewControllerFromXIB alloc] initWithText:self.tag];
        artikelViewController.artikelbestand = self.artikelbestand;
        artikelViewController.webviewrender  = YES;
        [self.navigationController pushViewController:artikelViewController animated:YES];
        [artikelViewController release];
        [query2 release];
        [results release];
        [sqlite dealloc];
        return;
      }
      ;
    }
    [query2 release];
    [results release];
    [sqlite dealloc];

    self.next_table = @"NoneShowArtikel";
  }

  if ([self.next_table compare:@"NoneShowArtikel"] == NSOrderedSame) {
    ArtikelViewControllerFromXIB *artikelViewController = [[ArtikelViewControllerFromXIB alloc] initWithText:self.tag];
    artikelViewController.artikelbestand = self.artikelbestand;
    [self.navigationController pushViewController:artikelViewController animated:YES];
    [artikelViewController release];
  }
  else{
    NSArray      *rowsarray = [sections objectAtIndex: currentIndexPath.section];
    NSDictionary *rowdicts  = [rowsarray objectAtIndex:currentIndexPath.row];
    NSString     *nt        = [rowdicts objectForKey:@"volgende"];

    if ([nt compare:@"wetboek"] == NSOrderedSame ||
        [nt compare:@"hoofdstukken"] == NSOrderedSame ||
        [nt compare:@"artikel"] == NSOrderedSame) {
      TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init];
      tableViewFromDatabaseController.table_name = self.next_table;
      tableViewFromDatabaseController.title      = @"Wetten";
      if ([self.next_table compare:@"wetboek"] == NSOrderedSame) {
        tableViewFromDatabaseController.currentID    = [NSString stringWithFormat:@"%d", cell.tag];
        tableViewFromDatabaseController.next_table   = @"hoofdstukken";
        tableViewFromDatabaseController.where_clause = [NSString stringWithFormat:@"where wetboekhoofdstuk_id=%d", cell.tag];
      }
      if ([self.next_table compare:@"hoofdstukken"] == NSOrderedSame) {
        tableViewFromDatabaseController.currentID    = [NSString stringWithFormat:@"%d", cell.tag];
        tableViewFromDatabaseController.next_table   = @"artikel";
        tableViewFromDatabaseController.where_clause = [NSString stringWithFormat:@"where wetboek_id=%d", cell.tag];

        Sqlite   *sqlite = [[Sqlite alloc] init];
        [sqlite open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]];
        NSString *query2  = [[NSString alloc] initWithFormat:@"select afk from wetboek where id='%d'", cell.tag];
        NSArray  *results = [sqlite executeQueryCopy: query2];
        tableViewFromDatabaseController.afkorting = [NSString stringWithFormat:@"%@", [[results objectAtIndex:0] objectForKey:@"afk"]];
        [query2 release];
        [sqlite release];
        [results release];
      }
      if ([self.next_table compare:@"artikel"] == NSOrderedSame) {
        tableViewFromDatabaseController.title = @"Artikelen";
        Sqlite *sqlite = [[Sqlite alloc] init];
        [sqlite open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]];
        query = [[NSString alloc] initWithFormat:@"select artikelbestand from hoofdstukken where id='%d'", cell.tag];
        NSArray *results = [sqlite executeQueryCopy: query];
        [sqlite release];
        for (NSDictionary *dictionary in results) {
          tableViewFromDatabaseController.artikelbestand = [dictionary objectForKey:@"artikelbestand"];
        }
        [results release];
        tableViewFromDatabaseController.where_clause = [NSString stringWithFormat:@"where hoofdstuk_id=%d", cell.tag];
        tableViewFromDatabaseController.next_table   = @"NoneShowArtikel";
      }

      tableViewFromDatabaseController.backbutton = tableViewFromDatabaseController.title;
      [tableViewFromDatabaseController reload];
      [self.navigationController pushViewController:tableViewFromDatabaseController animated:YES];
      [tableViewFromDatabaseController release];
    }
    else{
      /*
       * WebViewController *wvc = [ [ WebViewController alloc ] initWithText:self.tag ];
       * wvc.artikelbestand = nt;
       * [ self.navigationController pushViewController:wvc animated:YES ];
       * [ wvc release ];
       */
      ArtikelViewControllerFromXIB *artikelViewController = [[ArtikelViewControllerFromXIB alloc] initWithText:self.tag];
      artikelViewController.artikelbestand = nt;
      artikelViewController.webviewrender  = YES;
      [self.navigationController pushViewController:artikelViewController animated:YES];
      [artikelViewController release];
    }
  }
}


-(void) tableView: (UITableView *) tableView didSelectRowAtIndexPath: (NSIndexPath *) indexPath
{
  [self pushToNextScreen];
}

BOOL isPad()
{
#ifdef UI_USER_INTERFACE_IDIOM
  return(UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad) ;

#else
  return(NO) ;
#endif
}

-(UIView *) tableView: (UITableView *) tableView viewForHeaderInSection: (NSInteger) section
{
  if ([section_names count] == 0) {
    return(nil);
  }
  NSString           *sect_name = [section_names objectAtIndex:section];
  NSComparisonResult geentitel  = [sect_name compare:@"xxxxxxxx"];
  if (geentitel == NSOrderedSame) {
    return(nil);
  }

  // create the parent view that will hold header Label
  int                 width  = 300.0;
  UIDeviceOrientation orient = [UIDevice currentDevice].orientation;

  if (orient == UIDeviceOrientationLandscapeLeft || orient == UIDeviceOrientationLandscapeRight) {
    width = 480;
  }
  else{
    width = 300.0;
  }
  if (isPad()) {
    width = 700 ;
  }

  UIView      *customView = [[[UIView alloc] initWithFrame:CGRectMake(0.0, 0.0, width, 23.0)] autorelease];

  UIImageView *myimage = [[UIImageView alloc] initWithImage:[UIImage imageNamed:@"bg-sectionheader.png"]];

  [customView addSubview:myimage];
  [myimage release];

  // create the button object
  UILabel *headerLabel = [[UILabel alloc] initWithFrame:CGRectZero];
  headerLabel.backgroundColor      = [UIColor clearColor];
  headerLabel.opaque               = NO;
  headerLabel.textColor            = [UIColor whiteColor];
  headerLabel.highlightedTextColor = [UIColor whiteColor];
  headerLabel.shadowColor          = [UIColor darkGrayColor];
  CGSize s;
  s.width                  = 0;
  s.height                 = 1;
  headerLabel.shadowOffset = s;
  headerLabel.font         = [UIFont fontWithName: @"Helvetica-Bold" size: 17.0];
  headerLabel.frame        = CGRectMake(10.0, 0.0, width, 23.0);
  if ([section_names count] > section) {
    headerLabel.text = [section_names objectAtIndex:section];       // i.e. array element
  }
  else{
    headerLabel.text = @"error";
  }
  [customView addSubview:headerLabel];
  [headerLabel release];

  return(customView);
}

-(CGFloat) tableView: (UITableView *) tableView heightForHeaderInSection: (NSInteger) section
{
  return(23.0);
}


-(UITableViewCellEditingStyle) tableView: (UITableView *) tableView editingStyleForRowAtIndexPath: (NSIndexPath *) indexPath
{
  if ([self.table_name compare:@"bookmarks"] == NSOrderedSame) {
    return(UITableViewCellEditingStyleDelete);
  }
  else{
    return(UITableViewCellEditingStyleNone);
  }
}

-(void) tableView: (UITableView *) tableView commitEditingStyle: (UITableViewCellEditingStyle) editingStyle forRowAtIndexPath: (NSIndexPath *) indexPath
{
  if (editingStyle == UITableViewCellEditingStyleDelete &&[self.table_name compare:@"bookmarks"] == NSOrderedSame) {
    UITableViewCell *cell = [self.myTableView cellForRowAtIndexPath: indexPath];

    NSString        *databaseName  = @"bookmarks.db";
    NSArray         *documentPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
    NSString        *documentsDir  = [documentPaths objectAtIndex:0];
    NSString        *databasePath  = [documentsDir stringByAppendingPathComponent:databaseName];
    Sqlite          *sqlite        = [[Sqlite alloc] init];
    [sqlite open: databasePath];
    NSString        *query2  = [[NSString alloc] initWithFormat:@"delete from bookmarks where id='%d'", cell.tag];
    NSArray         *results = [sqlite executeQueryCopy:query2];
    [[sections objectAtIndex:0] removeObjectAtIndex: indexPath.section];
    NSMutableArray  *array = [[NSMutableArray alloc] init];
    [array addObject: indexPath];
    [self.myTableView deleteRowsAtIndexPaths: array withRowAnimation: UITableViewRowAnimationTop];
    [array release];
    [query2 release];
    [results release];
    [sqlite dealloc];
  }
}

-(void) viewDidLoad
{
  [super viewDidLoad];


  if ([self.table_name compare:@"bookmarks"] == NSOrderedSame) {
    self.navigationItem.rightBarButtonItem = [[[UIBarButtonItem alloc]
                                               initWithBarButtonSystemItem: UIBarButtonSystemItemEdit
                                               target: self
                                               action: @selector(startEditing)] autorelease];
  }
  else{
    UIBarButtonItem *barButtonItem = [[UIBarButtonItem alloc] initWithBarButtonSystemItem:UIBarButtonSystemItemSearch target:self action:@selector(search:)];
    self.navigationItem.rightBarButtonItem = barButtonItem;
    [barButtonItem release];
  }
}

-(void) didRotateFromInterfaceOrientation: (UIInterfaceOrientation) fromInterfaceOrientation
{
  [self.myTableView reloadData];
}

// Override to allow orientations other than the default portrait orientation.
-(BOOL) shouldAutorotateToInterfaceOrientation: (UIInterfaceOrientation) interfaceOrientation
{
  changedOrientation = YES;
  return(YES);
}

-(IBAction) showBookmarks: (id) sender
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init];

  tableViewFromDatabaseController.title        = @"Referenties";
  tableViewFromDatabaseController.backbutton   = self.title;
  tableViewFromDatabaseController.table_name   = @"bookmarks";
  tableViewFromDatabaseController.next_table   = @"artikel";
  tableViewFromDatabaseController.where_clause = @"";
  [tableViewFromDatabaseController reload];
  [self.navigationController pushViewController:tableViewFromDatabaseController animated:YES];
  [tableViewFromDatabaseController release];
}

-(void) setButtonsBottomBar
{
  self.backbtn.enabled    = NO;
  self.forwardbtn.enabled = NO;
  query                   = @"-777";

  NSComparisonResult compResult = [self.table_name compare:@"wetboek"];
  if (compResult == NSOrderedSame) {
    query = [[NSString alloc] initWithFormat:@"select first, last from wetboekhoofdstuk where id='%d'", [self.currentID integerValue]];
  }
  compResult = [self.table_name compare:@"hoofdstukken"];
  if (compResult == NSOrderedSame) {
    query = [[NSString alloc] initWithFormat:@"select first, last from wetboek where id='%d'", [self.currentID integerValue]];
  }

  compResult = [query compare:@"-777"];
  if (compResult != NSOrderedSame) {
    Sqlite  *sqlite = [[Sqlite alloc] init];
    [sqlite open:[[NSBundle mainBundle] pathForResource:@"wetten" ofType:@"db"]];
    NSArray *results = [sqlite executeQueryCopy:query];

    if ([results count] > 0) {
      if (0 ==[[[results objectAtIndex:0] objectForKey:@"first"] integerValue]) {
        self.backbtn.enabled = YES;
      }
      if (0 ==[[[results objectAtIndex:0] objectForKey:@"last"] integerValue]) {
        self.forwardbtn.enabled = YES;
      }
    }
    [results release];
    [sqlite release];
  }

  NSString *databaseName  = @"bookmarks.db";
  NSArray  *documentPaths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
  NSString *documentsDir  = [documentPaths objectAtIndex:0];
  NSString *databasePath  = [documentsDir stringByAppendingPathComponent:databaseName];
  Sqlite   *sqlite        = [[Sqlite alloc] init];
  [sqlite open: databasePath];
  query = @"SELECT id FROM bookmarks";
  NSArray *results = [sqlite executeQueryCopy:query];
  if ([results count] > 0) {
    if ([self.title compare:@"Referenties"] == NSOrderedSame) {
      self.bookmarkbtn.enabled = NO;
    }
    else{
      self.bookmarkbtn.enabled = YES;
    }
  }
  else{
    self.bookmarkbtn.enabled = NO;
  }
  [results release];
  [sqlite dealloc];

  if ([self.navigationController.viewControllers count] == 1) {
    self.homebtn.enabled = NO;
  }
}

-(void) viewWillAppear: (BOOL) animated
{
  NSIndexPath *selection = [self.myTableView indexPathForSelectedRow];

  if (selection) {
    [self.myTableView deselectRowAtIndexPath:selection animated:YES];
  }
  [super viewWillAppear:animated];
  [self setButtonsBottomBar];
  [self.myTableView setContentOffset:CGPointMake(0, 0) animated:NO];

  if ([self.table_name compare:@"hoofdstukken"] == NSOrderedSame) {
    UIBarButtonItem *newBackButton = [[UIBarButtonItem alloc] initWithTitle:self.afkorting style: UIBarButtonItemStyleBordered target: nil action: nil];
    [[self navigationItem] setBackBarButtonItem: newBackButton];
    [newBackButton release];
  }
}

-(IBAction) moveBack: (id) sender
{
  CATransition *myTransition = [CATransition animation];

  myTransition.timingFunction = UIViewAnimationCurveEaseInOut;
  myTransition.type           = kCATransitionPush;
  myTransition.subtype        = kCATransitionFromLeft;
  [self.myTableView.layer addAnimation:myTransition forKey: nil];

  self.backbtn.enabled = NO;
  query                = @"-777";
  NSComparisonResult compResult = [self.table_name compare:@"wetboek"];
  if (compResult == NSOrderedSame) {
    self.where_clause = [[NSString alloc] initWithFormat:@"where wetboekhoofdstuk_id=%d", [self.currentID integerValue] - 1];
  }
  compResult = [self.table_name compare:@"hoofdstukken"];
  if (compResult == NSOrderedSame) {
    self.where_clause = [[NSString alloc] initWithFormat:@"where wetboek_id=%d", [self.currentID integerValue] - 1];
  }
  self.currentID = [[NSString alloc] initWithFormat:@"%d", [self.currentID integerValue] - 1];
  [self reload];
  [self.myTableView reloadData];
  [self setButtonsBottomBar];
}

-(IBAction) moveForward: (id) sender
{
  CATransition *myTransition = [CATransition animation];

  myTransition.timingFunction = UIViewAnimationCurveEaseInOut;
  myTransition.type           = kCATransitionPush;
  myTransition.subtype        = kCATransitionFromRight;
  [self.myTableView.layer addAnimation:myTransition forKey: nil];

  self.forwardbtn.enabled = NO;
  query                   = @"-777";
  NSComparisonResult compResult = [self.table_name compare:@"wetboek"];
  if (compResult == NSOrderedSame) {
    self.where_clause = [[NSString alloc] initWithFormat:@"where wetboekhoofdstuk_id=%d", [self.currentID integerValue] + 1];
  }
  compResult = [self.table_name compare:@"hoofdstukken"];
  if (compResult == NSOrderedSame) {
    self.where_clause = [[NSString alloc] initWithFormat:@"where wetboek_id=%d", [self.currentID integerValue] + 1];
  }

  self.currentID = [[NSString alloc] initWithFormat:@"%d", [self.currentID integerValue] + 1];
  [self reload];
  [self.myTableView reloadData];
  [self setButtonsBottomBar];
}

-(void) didReceiveMemoryWarning
{
  [super didReceiveMemoryWarning];
}

-(IBAction) popToHome: (id) sender
{
  [self.navigationController popToRootViewControllerAnimated:YES];
}

-(IBAction) loadExoneratieController: (id) sender
{
  ExoneratieViewController *exoneratieViewController = [[ExoneratieViewController alloc] init];

  exoneratieViewController.title = @"Sociaalrecht 2009";
  [self.navigationController pushViewController:exoneratieViewController animated:YES];
  [exoneratieViewController release];
}

-(void) viewDidUnload
{
  // Release any retained subviews of the main view.
  // e.g. self.myOutlet = nil;
}

-(void) search: (id) sender
{
  WetboekSearchViewController *searchViewController = [[WetboekSearchViewController alloc] init];

  searchViewController.title = @"Zoeken";
  [self.navigationController pushViewController:searchViewController animated:YES];
  [searchViewController release];
}

-(void) dealloc
{
  [sections release];
  [section_names release];
  [rows release];
  [super dealloc];
}


@end
