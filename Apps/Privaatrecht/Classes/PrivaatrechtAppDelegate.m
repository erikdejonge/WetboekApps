//
//  PrivaatrechtAppDelegate.m
//  Privaatrecht
//
//  Created by rabshakeh on 10/27/09 - 2:07 PM.
//  Copyright __MyCompanyName__ 2010. All rights reserved.
//

#import "PrivaatrechtAppDelegate.h"
#import "PrivaatrechtViewController.h"
#import "TableViewFromDatabaseViewController.h"

@implementation PrivaatrechtAppDelegate

@synthesize window ;
@synthesize viewController ;

-(void) applicationDidFinishLaunching: (UIApplication *) application
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;

  tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk" ;
  tableViewFromDatabaseController.next_table = @"wetboek" ;
  tableViewFromDatabaseController.title      = @"Privaatrecht - Okt.2010" ;
  [tableViewFromDatabaseController reload] ;
  navigationController = [[UINavigationController alloc] initWithRootViewController:tableViewFromDatabaseController] ;

  [tableViewFromDatabaseController release] ;
  navigationController.navigationBar.tintColor = [UIColor colorWithRed:0.46 green:0.06 blue:0.13 alpha:0] ;

  [window addSubview:[navigationController view]] ;

  [window makeKeyAndVisible] ;
}


-(void) dealloc
{
  [navigationController release] ;
  [viewController release] ;
  [window release] ;
  [super dealloc] ;
}


@end
