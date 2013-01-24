//
//  TableViewFromDatabaseViewController.h
//  TableViewFromDatabase
//
//  Created by rabshakeh on 6/22/09 - 11:40 AM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface TableViewFromDatabaseViewController : UIViewController<UITableViewDelegate, UITableViewDataSource>
{
  NSMutableArray           *rows ;
  NSMutableArray           *sections ;
  NSMutableArray           *section_names ;
  NSString                 *currentID ;
  NSString                 *table_name ;
  NSString                 *table_id ;
  NSString                 *next_table ;
  NSString                 *where_clause ;
  NSString                 *query ;
  NSString                 *artikelbestand ;
  NSString                 *bevatartikelen ;
  NSString                 *backbutton ;
  NSString                 *afkorting ;
  NSString                 *tag ;
  IBOutlet UIBarButtonItem *bookmarkbtn ;
  IBOutlet UIBarButtonItem *exoneratieBtn ;
  IBOutlet UITableView     *myTableView ;
  NSIndexPath              *currentIndexPath ;
  NSLock                   *myLock ;
  bool                     changedOrientation ;
  IBOutlet UIBarButtonItem *backbtn ;
  IBOutlet UIBarButtonItem *forwardbtn ;
  IBOutlet UIBarButtonItem *homebtn ;
}

@property (retain, nonatomic) NSLock          *myLock ;
@property (retain, nonatomic) NSIndexPath     *currentIndexPath ;
@property (retain, nonatomic) NSString        *currentID ;
@property (retain, nonatomic) NSString        *table_name ;
@property (retain, nonatomic) NSString        *table_id ;
@property (retain, nonatomic) NSString        *next_table ;
@property (retain, nonatomic) NSString        *where_clause ;
@property (retain, nonatomic) NSString        *query ;
@property (retain, nonatomic) NSString        *artikelbestand ;
@property (retain, nonatomic) NSString        *bevatartikelen ;
@property (retain, nonatomic) NSString        *backbutton ;
@property (retain, nonatomic) NSString        *afkorting ;
@property (retain, nonatomic) NSString        *tag ;
@property (retain, nonatomic) UITableView     *myTableView ;
@property (retain, nonatomic) UIBarButtonItem *bookmarkbtn ;
@property (retain, nonatomic) UIBarButtonItem *exoneratieBtn ;
@property (retain, nonatomic) UIBarButtonItem *backbtn ;
@property (retain, nonatomic) UIBarButtonItem *forwardbtn ;
@property (retain, nonatomic) UIBarButtonItem *homebtn ;

-(void)reload ;

-(IBAction)popToHome                : (id)sender ;
-(IBAction)moveForward              : (id)sender ;
-(IBAction)moveBack                 : (id)sender ;
-(IBAction)loadExoneratieController : (id)sender ;
-(IBAction)showBookmarks            : (id)sender ;

@end

